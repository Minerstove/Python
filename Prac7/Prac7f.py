def consec_pairs(iter_seq):
    it = iter(iter_seq)
    try:
        prev = next(it)
    except StopIteration:
        return
    
    for curr in it:
        yield (prev, curr)
        prev = curr
        
assert [*consec_pairs((3, 1, 4, 1, 5))] == [(3, 1), (1, 4), (4, 1), (1, 5)], [*consec_pairs((3, 1, 4, 1, 5))]
assert [*consec_pairs([3])] == [], [*consec_pairs([3])]


