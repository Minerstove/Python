def neighs4(x,y):
    yield ((x , y + 1))
    yield ((x + 1, y))
    yield ((x, y - 1))
    yield ((x - 1, y))
    

assert [*neighs4(5, 2)] == [(5, 3), (6, 2), (5, 1), (4, 2)], [*neighs4(5, 2)]


