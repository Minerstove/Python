def grid_neighs4(r,c,i,j):
    yield (i - 1, j) if 0 <= i - 1 < r else None
    yield (i, j + 1) if 0 <= j + 1 < c else None
    yield (i + 1, j) if 0 <= i + 1 < r else None
    yield (i, j - 1) if 0 <= j - 1 < c else None
    
    

assert [*grid_neighs4(7, 5, 5, 2)] == [(4, 2), (5, 3), (6, 2), (5, 1)], [*grid_neighs4(7, 5, 5, 2)]
assert [*grid_neighs4(6, 3, 5, 2)] == [(4, 2), (5, 1)], [*grid_neighs4(6, 3, 5, 2)]





        

    