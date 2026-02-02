def maxes(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    
    while True:
        try:
            yield max(next(it1), next(it2))
        except StopIteration:
            return
    
assert [*maxes((1, 2, 3, 4, 5), (5, 4, 3, 2, 1))] == [5, 4, 3, 4, 5], [*maxes((1, 2, 3, 4, 5), (5, 4, 3, 2, 1))]
assert [*maxes((1, 2, 3), (4, 5, 6, 7, 8))] == [4,5,6], [*maxes((1, 2, 3), (4, 5, 6, 7, 8))]

