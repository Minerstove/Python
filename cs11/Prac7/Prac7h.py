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

# def segments(k,s):
#     a = [None,]*k
#     s = iter(s)
#     v = 0
#     for i in s:
#         if a[-1] == None:
#             a[v] = i
#             v+=1
#         else:
#             yield tuple(a)
#             a.pop(0)
#             a.append(i)
#     if a[-1] == None:
#        pass
#     else:
#         yield tuple(a)

assert [*segments(4, (3, 1, 4, 1, 5, 9))] == [(3, 1, 4, 1), (1, 4, 1, 5), (4, 1, 5, 9)], [*segments(4, (3, 1, 4, 1, 5, 9))]
assert [*segments(40, (3, 1, 4, 1, 5, 9))] == [], [*segments(40, (3, 1, 4, 1, 5, 9))]

