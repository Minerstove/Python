def patrol_heatmap(r, c, pts):
    # Initialize the grid
    heat = [[0] * c for _ in range(r)]

    # Count the very first cell
    si, sj = pts[0]
    heat[si][sj] += 1

    # Loop over every consecutive pair of points
    for k in range(len(pts) - 1):
        si, sj = pts[k]
        ti, tj = pts[k + 1]

        # Horizontal movement (left or right)
        if sj <= tj:
            for j in range(sj + 1, tj + 1):
                heat[si][j] += 1
        else:
            for j in range(sj - 1, tj - 1, -1):
                heat[si][j] += 1

        # Vertical movement (up or down)
        if si <= ti:
            for i in range(si + 1, ti + 1):
                heat[i][tj] += 1
        else:
            for i in range(si - 1, ti - 1, -1):
                heat[i][tj] += 1

    return heat



assert patrol_heatmap(5, 6, (
    (3, 4),
    (3, 1),
    (1, 4),
    (4, 1),
    (1, 5),
    (0, 3),
)) == [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 2, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 2, 2, 2, 2, 1],
    [0, 1, 1, 1, 1, 1],
], [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 2, 2, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 2, 2, 2, 2, 1],
    [0, 1, 1, 1, 1, 1],
]

assert patrol_heatmap(5, 6, (
    (0, 0),
    (0, 0),
    (0, 0),
)) == [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
], patrol_heatmap(5, 6, (
    (0, 0),
    (0, 0),
    (0, 0),
))
