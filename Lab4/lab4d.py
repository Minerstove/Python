def draw_bomb_traces(bombs, p, koyuki, n):
    rc = 2 * n + 1
    ky, kx = koyuki

    # make empty grid
    grid = []
    for _ in range(rc):
        row = list("." * rc)
        grid.append(row)

    # draw one diamond ring of radius p around each bomb
    for bi, bj in bombs:
        for dx in range(-p, p + 1):
            abs_dx = dx if dx >= 0 else -dx
            gap = p - abs_dx
            for dy in range(-gap, gap + 1):
                if abs_dx + (dy if dy >= 0 else -dy) == p:
                    y = bi + dy
                    x = bj + dx
                    sy = n + (y - ky)
                    sx = n + (x - kx)
                    if 0 <= sy < rc and 0 <= sx < rc:
                        grid[sy][sx] = "X"

    # build final string (no comprehensions)
    lines = []
    for row in grid:
        line = ""
        for ch in row:
            line = line + ch
        lines.append(line)

    result = ""
    for i in range(len(lines)):
        result = result + lines[i]
        if i != len(lines) - 1:
            result = result + "\n"
    result = result + "\n"

    return result



assert draw_bomb_traces(((1, 1), (3, 2)), 1, (2, 2), 2) == """\
.X...
X.X..
.XX..
.X.X.
..X..
""", draw_bomb_traces(((1, 1), (3, 2)), 1, (2, 2), 2)

assert draw_bomb_traces(((-4, 6), (-1, 14), (-4, 15)), 4, (-3, 8), 4) == """\
.X.X.....
X...X....
.....X..X
......XX.
.....X..X
X...X..X.
.X.X..X..
..X....X.
........X
""", draw_bomb_traces(((-4, 6), (-1, 14), (-4, 15)), 4, (-3, 8), 4)