def poss_locations(r, c):
    return frozenset(
        frozenset(((i, j), (k, l)))
            for i in range(r)
            for j in range(c)
            for k, l in neighs4(i, j)
            if inb(k, l, r, c)
    )

def inb(i, j, r, c):
    return 0 <= i < r and 0 <= j < c

def neighs4(i, j):
    return ((i + 1, j), (i, j + 1), (i, j - 1), (i - 1, j))

assert poss_locations(1, 2) == frozenset((
    frozenset(((0, 0), (0, 1))),
)), poss_locations(1, 2)
