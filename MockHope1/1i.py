def walks_in_the_park(r,c):
    goal = (r - 1, c - 1)

    def in_bounds(i, j):
        return 0 <= i < r and 0 <= j < c
    
    def get_neighbors(cell):

        i, j = cell[0], cell[1]

        return tuple(
            (i + di, j + dj)
            for di, dj in ((0,1), (1,0), (-1,0), (0, -1))
            if in_bounds(i + di, j + dj)
            )

    def path_maker(cell, visited, path):
        if cell == goal:
            return frozenset((tuple(path),))
        
        neighs = tuple(n for n in get_neighbors(cell) if n not in visited)

        def grow(idx):
            if idx == len(neighs):
                
                return frozenset()
            
            nxt = neighs[idx]
            
            taken = path_maker(
                nxt,
                visited | frozenset((nxt,)),   # no .add(); use immutable union operator
                path + (nxt,)                  # no append(); use tuple concat
            )
            # branch: skip nxt, move to next neighbor
            rest = grow(idx + 1)
            return taken | rest

        return grow(0)
           
    return path_maker((0,0), frozenset(((0,0),)), ((0,0),))

assert walks_in_the_park(2, 3) == frozenset((
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    ((0, 0), (0, 1), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2)),
)), walks_in_the_park(2, 3)

