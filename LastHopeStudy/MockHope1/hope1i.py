def walks_in_the_park(r, c):
    def helper(i, j, visited):
        if i < 0 or i >= r or j < 0 or j >= c:
            return frozenset()
        
        if i == r - 1 and j == c - 1:
            return frozenset((visited + ((i, j),),))
        
        if i >= r or j >= c:
            return frozenset()
        
        if (i, j) in visited:
            return frozenset()
        
        right = helper(i + 1, j, visited + ((i, j),))
        down = helper(i, j - 1, visited + ((i, j),))
        up = helper(i, j + 1, visited + ((i, j),))
        left = helper(i - 1, j, visited + ((i, j),))

        return right | down | up | left
    
    return helper(0, 0, ())

assert walks_in_the_park(2, 3) == frozenset((
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)),
)), walks_in_the_park(2, 3)
