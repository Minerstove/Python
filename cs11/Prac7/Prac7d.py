def drop(d,iter_seq):
    for i in iter_seq:
        if i + 1 > d:
            yield iter_seq[i]

assert [*drop(3, (3, 1, 4, 1, 5, 9, 2))] == [1,5,9,2], [*drop(3, (3, 1, 4, 1, 5, 9, 2))]
assert [*drop(30, (3, 1, 4, 1, 5, 9, 2))] == [], [*drop(30, (3, 1, 4, 1, 5, 9, 2))]
