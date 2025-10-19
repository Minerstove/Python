def grid_neighs4(r,c,i,j):
    for ni, nj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if (0 <= i + ni < r) and (0 <= j + nj < c):
            yield (i + ni, j + nj)