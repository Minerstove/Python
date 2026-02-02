def move2d(coords, moves):
    x, y = coords
    index = 0

    yield (x, y)
    for move in moves:
        if index % 4 == 0:
            y += move
        elif index % 4 == 1:
            x += move
        elif index % 4 == 2:
            y -= move
        else:
            x -= move
        
        index += 1

        yield (x,y)

assert [*move2d((-1, 1), (3, 2, 2, 3, 1, 4))] == [
    (-1, 1),
    (-1, 4),
    (1, 4),
    (1, 2),
    (-2, 2),
    (-2, 3),
    (2, 3),
],[*move2d((-1, 1), (3, 2, 2, 3, 1, 4))]

assert [*move2d((5, 5), iter([]))] == [(5, 5)],[*move2d((5, 5), iter([]))]

