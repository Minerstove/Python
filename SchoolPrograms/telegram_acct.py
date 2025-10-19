"""
Telegram Poll Reader (Python)

Two approaches:
1) BOT API (python-telegram-bot): capture live poll updates and build a voter roster (for non‑anonymous polls) or counts (for anonymous).
2) TELETHON (user account): read an existing poll by chat + message link/ID and export results to CSV, including voters for non‑anonymous polls.

Create a virtualenv and install deps:
    pip install python-telegram-bot==21.6 telethon==1.36.0 python-dotenv==1.0.1

Set env vars in a .env file as needed.
"""

# ==============================
# 1) BOT API: Live Poll Collector
# ==============================

import os
import csv
import json
import asyncio
from datetime import datetime
from typing import Dict, Any, List

from dotenv import load_dotenv

# NOTE: python-telegram-bot v21 is async-only
from telegram import Update, Poll, PollOption, User
from telegram.ext import (Application, PollHandler, PollAnswerHandler,
                          CommandHandler, ContextTypes)

load_dotenv()

DATA_DIR = os.environ.get("TPR_DATA_DIR", "./tpr_data")
BOT_TOKEN = os.environ.get("7606673931:AAHuKO8z9O8mNcQ6t4VxF7MyKR6ONWlThyw", "")

os.makedirs(DATA_DIR, exist_ok=True)

# In-memory store: poll_id -> poll_data
POLL_STORE: Dict[str, Dict[str, Any]] = {}


def _poll_path(poll_id: str) -> str:
    return os.path.join(DATA_DIR, f"poll_{poll_id}.json")


def _csv_path(poll_id: str) -> str:
    return os.path.join(DATA_DIR, f"poll_{poll_id}.csv")


def save_poll(poll_id: str) -> None:
    path = _poll_path(poll_id)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(POLL_STORE[poll_id], f, ensure_ascii=False, indent=2, default=str)


def load_poll(poll_id: str) -> Dict[str, Any]:
    path = _poll_path(poll_id)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            POLL_STORE[poll_id] = json.load(f)
            return POLL_STORE[poll_id]
    raise FileNotFoundError(f"No saved poll {poll_id}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Hi! Add me to your group and create a NON‑ANONYMOUS poll.\n"
        "I'll track votes live. Commands:\n"
        "/status <poll_id> – show current tally\n"
        "/export <poll_id> – export CSV of votes (non‑anonymous)\n"
        "/load <poll_id> – load saved poll into memory\n"
        "/list – list known poll_ids"
    )


async def on_poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    poll: Poll = update.poll
    # Build our poll data structure on first sight
    if poll.id not in POLL_STORE:
        POLL_STORE[poll.id] = {
            "poll_id": poll.id,
            "question": poll.question,
            "is_anonymous": poll.is_anonymous,
            "allows_multiple_answers": poll.allows_multiple_answers,
            "options": [opt.text for opt in poll.options],
            "correct_option_id": poll.correct_option_id,
            "created_at": datetime.utcnow().isoformat(),
            # voters: user_id -> {"name": str, "option_ids": [int]}
            "voters": {},
            # last known counts per option index
            "counts": [opt.voter_count for opt in poll.options],
        }
    else:
        # Update counts if we already know this poll
        POLL_STORE[poll.id]["counts"] = [opt.voter_count for opt in poll.options]

    save_poll(poll.id)


async def on_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ans = update.poll_answer
    poll_id = ans.poll_id

    # Create placeholder if we somehow missed the Poll update
    if poll_id not in POLL_STORE:
        POLL_STORE[poll_id] = {
            "poll_id": poll_id,
            "question": "",
            "is_anonymous": None,
            "allows_multiple_answers": None,
            "options": [],
            "correct_option_id": None,
            "created_at": datetime.utcnow().isoformat(),
            "voters": {},
            "counts": [],
        }

    # Record the vote per user
    uid = ans.user.id
    name = f"{ans.user.first_name or ''} {ans.user.last_name or ''}".strip()
    POLL_STORE[poll_id]["voters"][str(uid)] = {
        "name": name or ans.user.username or str(uid),
        "option_ids": ans.option_ids,
    }

    save_poll(poll_id)


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /status <poll_id>")
        return
    poll_id = context.args[0]
    try:
        data = POLL_STORE.get(poll_id) or load_poll(poll_id)
    except FileNotFoundError:
        await update.message.reply_text("Poll not found in memory or disk.")
        return

    options = data.get("options", [])
    counts = data.get("counts", [])
    question = data.get("question", "(unknown question)")

    # Recompute counts from voters if possible and non-anonymous
    voters = data.get("voters", {})
    if voters and options:
        recomputed = [0] * len(options)
        for v in voters.values():
            for oid in v.get("option_ids", []):
                if 0 <= oid < len(options):
                    recomputed[oid] += 1
        counts = recomputed

    lines = [f"❓ {question}", f"poll_id: {poll_id}"]
    for i, opt in enumerate(options):
        c = counts[i] if i < len(counts) else 0
        lines.append(f"• [{i}] {opt}: {c}")

    total = sum(counts) if counts else 0
    lines.append(f"Total votes: {total}")

    await update.message.reply_text("\n".join(lines))


async def cmd_export(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /export <poll_id>")
        return
    poll_id = context.args[0]
    try:
        data = POLL_STORE.get(poll_id) or load_poll(poll_id)
    except FileNotFoundError:
        await update.message.reply_text("Poll not found in memory or disk.")
        return

    # If anonymous, we can only export aggregate counts
    if data.get("is_anonymous", True):
        # aggregate CSV: option, count
        path = _csv_path(poll_id)
        options = data.get("options", [])
        counts = data.get("counts", [0] * len(options))
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["option_index", "option", "count"])
            for i, opt in enumerate(options):
                c = counts[i] if i < len(counts) else 0
                w.writerow([i, opt, c])
        await update.message.reply_document(path, caption="Anonymous poll – aggregate counts only.")
        return

    # Non-anonymous: export voter roster with selected options
    voters = data.get("voters", {})
    options = data.get("options", [])

    path = _csv_path(poll_id)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        head = ["user_id", "name", "selected_indices", "selected_options"]
        w.writerow(head)
        for uid, v in voters.items():
            idxs: List[int] = v.get("option_ids", [])
            labels = [options[i] for i in idxs if 0 <= i < len(options)]
            w.writerow([uid, v.get("name", ""), ";".join(map(str, idxs)), ";".join(labels)])

    await update.message.reply_document(path, caption="Exported voter roster.")


async def cmd_load(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /load <poll_id>")
        return
    poll_id = context.args[0]
    try:
        data = load_poll(poll_id)
        await update.message.reply_text(f"Loaded poll {poll_id}: {data.get('question','')}")
    except FileNotFoundError as e:
        await update.message.reply_text(str(e))


async def cmd_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ids = list(POLL_STORE.keys())
    # Add those on disk
    for name in os.listdir(DATA_DIR):
        if name.startswith("poll_") and name.endswith(".json"):
            pid = name[len("poll_"):-len(".json")]
            if pid not in ids:
                ids.append(pid)
    if not ids:
        await update.message.reply_text("No polls known yet.")
    else:
        await update.message.reply_text("Known poll_ids:\n" + "\n".join(ids))


async def run_bot() -> None:
    if not BOT_TOKEN:
        print("[!] Set BOT_TOKEN in environment or .env first.")
        return

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("export", cmd_export))
    app.add_handler(CommandHandler("load", cmd_load))
    app.add_handler(CommandHandler("list", cmd_list))
    app.add_handler(PollHandler(on_poll))
    app.add_handler(PollAnswerHandler(on_poll_answer))

    print("[BOT] Running… Press Ctrl+C to stop.")
    await app.run_polling(close_loop=False)


# ==============================================
# 2) TELETHON: Scrape an Existing Poll by Message
# ==============================================

from telethon import TelegramClient
from telethon.tl import functions, types

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", "tpr_session")  # will create/ask login on first run


async def telethon_export_poll(chat: str, msg_id: int, out_csv: str) -> None:
    """Fetch a poll by chat and message id; export counts and (if non‑anonymous) voters."""
    async with TelegramClient(SESSION, API_ID, API_HASH) as client:
        msg = await client.get_messages(chat, ids=msg_id)
        if not msg or not getattr(msg, 'poll', None):
            raise RuntimeError("Message is not a poll.")

        poll: types.Poll = msg.poll
        results: types.PollResults = msg.results

        options: List[types.PollAnswer] = poll.answers
        # Aggregate counts per option (works for anonymous & non-anonymous)
        counts_by_opt: Dict[int, int] = {}
        for i, ans in enumerate(options):
            counts_by_opt[i] = 0
        if results and results.results:
            for r in results.results:  # type: types.PollAnswerVoters
                # r.option is bytes matching the option.data; we align by index
                # Find matching index:
                idx = next((i for i, a in enumerate(options) if a.option == r.option), None)
                if idx is not None:
                    counts_by_opt[idx] = r.voters

        # Write counts first
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["section", "option_index", "option_text", "count_or_user_id", "name_or_selected_indices"])
            for i, ans in enumerate(options):
                w.writerow(["counts", i, ans.text, counts_by_opt.get(i, 0), ""])

        # If NON‑anonymous, fetch voters per option using API (paginated)
        if not poll.public_voters:
            # poll.public_voters == False means ANONYMOUS
            print("[Telethon] Anonymous poll: only counts exported.")
            return

        async with TelegramClient(SESSION, API_ID, API_HASH) as client2:
            with open(out_csv, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                for i, ans in enumerate(options):
                    offset = None
                    while True:
                        res = await client2(functions.messages.GetPollVotesRequest(
                            peer=chat,
                            id=msg_id,
                            option=ans.option,
                            limit=100,
                            offset=offset
                        ))
                        for v in res.votes:
                            user: types.User = v.user
                            name = (f"{user.first_name or ''} {user.last_name or ''}".strip() or
                                    user.username or str(user.id))
                            w.writerow(["voters", i, ans.text, user.id, name])
                        if not res.next_offset:
                            break
                        offset = res.next_offset


async def main() -> None:
    mode = os.environ.get("TPR_MODE", "bot")  # "bot" or "telethon"
    if mode == "telethon":
        chat = os.environ.get("TPR_CHAT", "")
        msg_id = int(os.environ.get("TPR_MSG_ID", "0"))
        out = os.environ.get("TPR_OUT", "./tpr_poll.csv")
        if not (API_ID and API_HASH and chat and msg_id):
            print("[!] Set API_ID, API_HASH, TPR_CHAT, TPR_MSG_ID in env for telethon mode.")
            return
        await telethon_export_poll(chat, msg_id, out)
        print(f"[Telethon] Exported to {out}")
    else:
        await run_bot()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
