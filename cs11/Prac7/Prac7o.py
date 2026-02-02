def interleave(*params):
    pool = [iter(s) for s in params]

    while pool:
        it = pool.pop(0)
        try:
            val = next(it)
        except StopIteration:
            pass
        else:
            yield val
            pool.append(it)
            

assert [*interleave((3, 1, 4), (2, 7, 1), (1, 4, 1))] == [3, 2, 1, 1, 7, 4, 4, 1, 1], [*interleave((3, 1, 4), (2, 7, 1), (1, 4, 1))]
assert [*interleave((3, 1, 4, 1, 5), (2, 7, 1), (1, 4, 1, 4, 2, 1, 3))] == [3, 2, 1, 1, 7, 4, 4, 1, 1, 1, 4, 5, 2, 1, 3], [*interleave((3, 1, 4, 1, 5), (2, 7, 1), (1, 4, 1, 4, 2, 1, 3))]
assert [*interleave((3, 1, 4, 1, 5))] == [3, 1, 4, 1, 5],[*interleave((3, 1, 4, 1, 5))]
assert [*interleave()] == [], [*interleave()]