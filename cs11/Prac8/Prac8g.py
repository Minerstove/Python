def bishop_threats(grid):
    g = [list(row) for row in grid]
    r = len(grid)
    c = len(grid[0])

    bishop_coords = [(x, y) for y, row in enumerate(g) for x, ch in enumerate(row) if ch == "#"]

    dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for bx, by in bishop_coords:
        for nx, ny in dirs:
            x, y = bx + nx, by + ny
            while 0 <= y < r and 0 <= x < c:
                if g[y][x] == "#":
                    break
                g[y][x] = "*"
                x += nx
                y += ny
    
    return["".join(row) for row in g]

assert bishop_threats((
    '...........#.',
    '.............',
    '.............',
    '..#..........',
    '............#',
    '.............',
    '.............',
    '......#......',
)) == [
    '.....*..*..#.',
    '*...*....**.*',
    '.*.*.....***.',
    '..#.....*.**.',
    '.*.*...*.*..#',
    '*...*.*.*..*.',
    '.....*.*..*..',
    '....*.#..*...',
],bishop_threats((
    '...........#.',
    '.............',
    '.............',
    '..#..........',
    '............#',
    '.............',
    '.............',
    '......#......',
))
