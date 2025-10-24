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


# def consec_pairs(_ints):
#     ints = iter(_ints)
#     another_helper = iter(_ints)
#     next(another_helper)
#     for num in ints:
#         try:
#             yield (num, next(another_helper))
#         except StopIteration:
#             break

# assert [*consec_pairs((3, 1, 4, 1, 5))] == [(3, 1), (1, 4), (4, 1), (1, 5)], [*consec_pairs((3, 1, 4, 1, 5))]
# assert [*consec_pairs([3])] == [], [*consec_pairs([3])]