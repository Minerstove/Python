def trace(matrix):
    diagonals = []
    index = 0

    for row in matrix:
        diagonals.append(row[index])
        index += 1

    return sum(diagonals)

assert trace((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)) == 15, trace((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
))


