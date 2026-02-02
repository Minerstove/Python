def interleave(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)

    while True:
        try:
            yield next(it1)
        except StopIteration:
            try:
                yield next(it2)
            except StopIteration:
                return
        
        try: 
            yield next(it2)
        except StopIteration:
            try:
                yield next(it1)
            except StopIteration:
                return

assert [*interleave((3, 1, 4), (2, 7, 1))] == [3, 2, 1, 7, 4, 1], [*interleave((3, 1, 4), (2, 7, 1))]
assert [*interleave((3, 1, 4, 1, 5), (2, 7, 1))] == [3, 2, 1, 7, 4, 1, 1, 5], [*interleave((3, 1, 4, 1, 5), (2, 7, 1))]
assert [*interleave((3, 1, 4), (2, 7, 1, 8, 2))] == [3, 2, 1, 7, 4, 1, 8, 2], [*interleave((3, 1, 4), (2, 7, 1, 8, 2))]



