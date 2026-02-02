def consec_triples(iter_seq):
    it = iter(iter_seq)
    try:
        first = next(it)
        second = next(it)
    except StopIteration:
        return
    
    for curr in it:
        yield (first, second, curr)
        first = second
        second = curr

assert [*consec_triples((3, 1, 4, 1, 5))] == [(3, 1, 4), (1, 4, 1), (4, 1, 5)], [*consec_triples((3, 1, 4, 1, 5))]
assert [*consec_triples([3])] == [], [*consec_triples([3])]
