#Lab 2c - Koyuki and Bombs 2
def cells_caught_in_blasts(bs, p):
    return frozenset(
        (bi + dx, bj + dy)
        for bi, bj in bs
        for dx in range(-p, p + 1)
        for dy in ((p - abs(dx),) if p == abs(dx) else (-(p - abs(dx)), p - abs(dx)))
    )

#print(cells_caught_in_blasts(((0, 0), (1, 1)), 1))

#Lab 2d - Koyuki and Bombs 3
def possible_bomb_positions(ts, p):
    if not ts:
        return frozenset()

    if p == 0:
        return frozenset((ts[0]),) if all(cell == ts[0] for cell in ts) else frozenset()

    if any(
        abs(ti - ui) + abs(tj - uj) > 2 * p
        for (ti, tj) in ts
        for (ui, uj) in ts
    ):
        return frozenset()

    if len(frozenset((ti + tj) % 2 for (ti, tj) in ts)) > 1:
        return frozenset()

    ti0, tj0 = ts[0]
    candidates = frozenset(
        (ti0 + dx, tj0 + dy)
        for dx in range(-p, p + 1)
        for dy in ((p - abs(dx),) if p == abs(dx) else (-(p - abs(dx)), p - abs(dx)))
    )

    if len(ts) == 1:
        return candidates

    return frozenset(
        (bi, bj)
        for (bi, bj) in candidates
        if all(abs(bi - ti) + abs(bj - tj) == p for (ti, tj) in ts)
    )



print(possible_bomb_positions(((0, 0), (1, 1)), 1))