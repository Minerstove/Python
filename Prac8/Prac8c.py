def wrap(text, c):
    text = text_fixer(text)
    words = text.split(" ")
    lines = []
    line = ""
    for w in words:
        if not line:
            line = w
        elif len(line) + 1 + len(w) <= c:
            line += " " + w
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines
def text_fixer(text):
    out = []
    i, n = 0, len(text)
    punct = ".,!?;:"

    while i < n:
        ch = text[i]
        if ch in " \n":
            j = i
            while j < n and text[j] in " \n":
                j += 1
            prev = out[-1] if out else ""
            nextch = text[j] if j < n else ""
            if prev and prev != " " and nextch and nextch not in punct:
                out.append(" ")
            i = j
            continue
        if ch in punct:
            if out and out[-1] == " ":
                out.pop()
            out.append(ch)
            i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out).strip()



assert wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 25) == [
    "They were all dead. The",
    "final gunshot was an",
    "exclamation mark on",
    "everything that had led",
    "to this point. I released",
    "my finger from the",
    "trigger, and then it was",
    "over.",
], wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 25)

assert wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 16) == [
    "They were all",
    "dead. The final",
    "gunshot was an",
    "exclamation mark",
    "on everything",
    "that had led to",
    "this point. I",
    "released my",
    "finger from the",
    "trigger, and",
    "then it was",
    "over.",
], wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 16)

assert wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 9) == [
    "They were",
    "all dead.",
    "The final",
    "gunshot",
    "was an",
    "exclamation",
    "mark on",
    "everything",
    "that had",
    "led to",
    "this",
    "point. I",
    "released",
    "my finger",
    "from the",
    "trigger,",
    "and then",
    "it was",
    "over.",
], wrap("""They were all dead.

The final   gunshot
was an exclamation mark on everything that had led to this point.   I released
my
finger  from  the  trigger,
and then it was over.
""", 9)





