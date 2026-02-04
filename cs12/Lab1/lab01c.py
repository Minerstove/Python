# Lab 1c – 7-Segment Display

LINES: list[str] = ["    ", " -- ", "|   ", "   |", "|  |"]
DIGITS: list[tuple[int, ...]] = [
    (1, 4, 0, 4, 1), # zero
    (0, 3, 0, 3, 0), # one
    (1, 3, 1, 2, 1), # two
    (1, 3, 1, 3, 1), # three
    (0, 4, 1, 3, 0), # four
    (1, 2, 1, 3, 1), # five
    (1, 2, 1, 4, 1), # six
    (1, 3, 0, 3, 0), # seven
    (1, 4, 1, 4, 1), # eight
    (1, 4, 1, 3, 1), # nine
]

def display(value: int) -> list[str]:
    output: list[str] = ["", "", "", "", ""]
    s: str = str(value)
    while s:
        digit: int = int(s[-1])
        output = [LINES[DIGITS[digit][ind]] + output[ind] for ind in range(5)]
        # add space if another digit is expected
        if len(s) > 1:
            output = [" " + r for r in output]
        s = s[:-1]
    return output