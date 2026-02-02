def spread_d(d, grid):
    listed_grid = list(list(row) for row in grid)
    
    sculk_coords = set()
    for y in range(len(listed_grid)):
        for x in range(len(listed_grid[y])):
            if listed_grid[y][x] == "X":
                sculk_coords.add((x, y))

    for _ in range(d):
        new_sculk_coords = set()
        
        for x, y in sculk_coords:
            for nx, ny in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                if 0 <= ny < len(listed_grid) and 0 <= nx < len(listed_grid[ny]):
                    if listed_grid[ny][nx] != "#" and listed_grid[ny][nx] != "X":
                        listed_grid[ny][nx] = "X"
                        new_sculk_coords.add((nx,ny))
        
        sculk_coords = new_sculk_coords
        if not sculk_coords:
            break

    return ["".join(row) for row in listed_grid]

assert spread_d(1, (
    '.....X',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
)) == [
    '.X..XX',
    'XXX..#',
    '.X.X#.',
    '..#XX.',
    '.X.#..',
    'XXXXX.',
    'XXXX..',
], spread_d(1, (
    '.....X',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
))

assert spread_d(2, (
    '.....X',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
)) == [
    'XXXXXX',
    'XXXXX#',
    'XXXX#.',
    '.X#XXX',
    'XXX#X.',
    'XXXXXX',
    'XXXXX.',
], spread_d(2, (
    '.....X',
    '.X...#',
    '....#.',
    '..#X..',
    '...#..',
    '.X.X..',
    '.X....',
))
