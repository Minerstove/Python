from collections.abc import Sequence

def min_to_pass(scores: Sequence[int]) -> int:
    n = len(scores)
    needed = 60 * (n + 1) - sum(scores)

    if needed > 100:
        return -1
    if needed < 0:
        return 0
    return needed