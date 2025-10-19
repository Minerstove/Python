def increasing_appearances(seq):
    for i, val in enumerate(seq, start=1):
        yield from (val for _ in range(i))

assert [*increasing_appearances((3, 1, 4))] == [3, 1, 1, 4, 4, 4], [*increasing_appearances((3, 1, 4))]