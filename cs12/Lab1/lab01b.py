from collections.abc import Sequence

Grid = Sequence[str]
N_Grid = list[list[str]]

def move_around(grid: Grid, moves: str) -> list[str]:
    new_grid: N_Grid = [list(row) for row in grid]
    move_dict = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    for char in moves:
        di, dj = move_dict[char]

        pieces = piece_scanner(new_grid)
        targets = [(i + di, j + dj) for (i, j) in pieces]

        if not all(valid_move(new_grid, ti, tj) for (ti, tj) in targets):
            continue

        if len(set(targets)) != len(targets):  # collision
            continue

        temp_grid = [row[:] for row in new_grid]  # deep copy rows
        for (i, j) in pieces:
            temp_grid[i][j] = "."
        for (ti, tj) in targets:
            temp_grid[ti][tj] = "#"

        new_grid = temp_grid

    return ["".join(row) for row in new_grid]

def valid_move(grid: N_Grid, ci: int, cj: int) -> bool:
    r: int = len(grid)
    c: int = len(grid[0])
    return 0 <= ci < r and 0 <= cj < c and grid[ci][cj] != "x"


def piece_scanner(grid: N_Grid) -> list[tuple[int, int]]:
    r: int = len(grid)
    c: int = len(grid[0])
    pieces: list[tuple[int, int]] = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "#":
                pieces.append((i, j))
    return pieces
