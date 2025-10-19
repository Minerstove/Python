import os
from dotenv import load_dotenv, find_dotenv

# Always load the .env next to this file, not just the CWD
_here = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(_here, ".env")
if not os.path.exists(dotenv_path):
    # Fall back to searching upwards from CWD
    dotenv_path = find_dotenv()

load_dotenv(dotenv_path=dotenv_path, override=True)

# DEBUG: print where we loaded from and whether BOT_TOKEN exists
print(f"[dotenv] loaded: {dotenv_path}")
print(f"[dotenv] BOT_TOKEN present? {'yes' if os.environ.get('BOT_TOKEN') else 'no'}")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
if not BOT_TOKEN:
    raise RuntimeError("[!] Set BOT_TOKEN in environment or .env first.")

