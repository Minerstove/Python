def segments(k, iter_seq):
    it = iter(iter_seq)
    window = []

    try:
        for i in range(k):
            window.append(next(it))
        yield tuple(window)
    except StopIteration:
        return
    
    for curr in it:
        del window[0]
        window = window + [curr]
        yield tuple(window)

assert [*segments(4, (3, 1, 4, 1, 5, 9))] == [(3, 1, 4, 1), (1, 4, 1, 5), (4, 1, 5, 9)], [*segments(4, (3, 1, 4, 1, 5, 9))]
assert [*segments(40, (3, 1, 4, 1, 5, 9))] == [], [*segments(40, (3, 1, 4, 1, 5, 9))]

