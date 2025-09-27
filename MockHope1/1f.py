def splits2(toys):
    if not toys:
        return frozenset((((), ()),))
    
    first, rest = toys[0], toys [1:]
    smaller = splits2(rest)

    seq = tuple(smaller)

    def grow(lo, hi):
        if lo == hi:
            return frozenset()
        if hi - lo == 1:
            k, h = seq[lo]
            give_king  = ((first,) + k, h)
            give_harry = (k, (first,) + h)
            return frozenset((give_king, give_harry))
        mid = (lo + hi) // 2
        left  = grow(lo, mid)
        right = grow(mid, hi)
        print(left.union(right))
        return left.union(right)

    print("splits2 called with:", toys)

    return grow(0, len(seq))

"""assert splits2(('ball', 'yoyo', 'jigsaw')) == frozenset((
    (('jigsaw',), ('ball', 'yoyo')),
    (('ball',), ('yoyo', 'jigsaw')),
    ((), ('ball', 'yoyo', 'jigsaw')),
    (('ball', 'yoyo'), ('jigsaw',)),
    (('ball', 'yoyo', 'jigsaw'), ()),
    (('ball', 'jigsaw'), ('yoyo',)),
    (('yoyo', 'jigsaw'), ('ball',)),
    (('yoyo',), ('ball', 'jigsaw')),
)), splits2(('ball', 'yoyo', 'jigsaw'))"""

print(splits2((tuple(char for char in "abcdefghijklmno"))))


