def splits2(toys):
    def helper(index, left, right):
        if index ==  len(toys):
            return frozenset(((left, right),))
        
        # Imagine that this basically splits into two nodes
        left_splits = helper(index + 1, left + (toys[index],), right)
        right_splits = helper(index + 1, left, right + (toys[index],))

        return left_splits | right_splits
    
    return helper(0, (), ())

assert splits2(('ball', 'yoyo', 'jigsaw')) == frozenset((
    (('jigsaw',), ('ball', 'yoyo')),
    (('ball',), ('yoyo', 'jigsaw')),
    ((), ('ball', 'yoyo', 'jigsaw')),
    (('ball', 'yoyo'), ('jigsaw',)),
    (('ball', 'yoyo', 'jigsaw'), ()),
    (('ball', 'jigsaw'), ('yoyo',)),
    (('yoyo', 'jigsaw'), ('ball',)),
    (('yoyo',), ('ball', 'jigsaw')),
)), splits2(('ball', 'yoyo', 'jigsaw'))

