def spread(grid):
    listed_grid = list(list(row) for row in grid)

    sculk_coords = []
    for y in range(len(listed_grid)):
        for x in range(len(listed_grid[y])):
            if listed_grid[y][x] == "X":
                sculk_coords.append((x, y))
    
    for x, y in sculk_coords:
        for nx, ny in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
            if 0 <= ny < len(listed_grid) and 0 <= nx < len(listed_grid[ny]):
                if listed_grid[ny][nx] != "#":
                    listed_grid[ny][nx] = "X"

    return ["".join(row) for row in listed_grid]



assert spread((
    '......',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
)) == [
    '.X....',
    'XXX..#',
    '.X.X#.',
    '..#XX.',
    '.X.#..',
    'XXXXX.',
    'XXXX..',
], spread((
    '......',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
))


