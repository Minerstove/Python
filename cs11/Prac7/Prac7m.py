def grid_neighs8(r,c,i,j):
    for ni, nj in ((1, 0), (1, -1), (0, 1), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        if (0 <= i + ni < r) and (0 <= j + nj < c):
            yield (i + ni, j + nj)

assert [*grid_neighs8(7, 5, 5, 2)] == [(4, 2), (4, 3), (5, 3), (6, 3), (6, 2), (6, 1), (5, 1), (4, 1)], [*grid_neighs8(7, 5, 5, 2)]
assert [*grid_neighs8(6, 3, 5, 2)] == [(4, 2), (5, 1), (4, 1)], [*grid_neighs8(6, 3, 5, 2)]



# UGHASLKHJKLJ just reorder the tuple bruh why couldnt it be qa set