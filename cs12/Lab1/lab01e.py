# Lab 1e – Drawing Whirlpools
from oj import Corner, Direction

TLD = {Direction.RIGHT: "R", Direction.DOWN: "D", Direction.LEFT: "L", Direction.UP: "U"}
TLC = {Corner.TOP_LEFT: "TL", Corner.TOP_RIGHT: "TR", Corner.BOTTOM_LEFT: "BL", Corner.BOTTOM_RIGHT: "BR"}
ROTATE = {"R": "D", "D": "L", "L": "U", "U": "R"}
DISTANCE = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def valid_direction(grid: list[list[str]], pos: tuple[int, int]) -> bool:

    # Check whether this is in bounds
    if not ((0 <= pos[0] < len(grid)) and (0 <= pos[1] < len(grid[0]))): return False

    # Check whether this is occupied
    if grid[pos[0]][pos[1]] == '#': return False

    # At this point, must be a valid, empty space.
    # Check for loop closes
    connections: int = 0
    for d in ("U", "D", "L", "R"):
        if (0 <= (pos[0] + DISTANCE[d][0]) < len(grid)) and (0 <= (pos[1] + DISTANCE[d][1]) < len(grid[0])):
            if grid[pos[0] + DISTANCE[d][0]][pos[1] + DISTANCE[d][1]] == '#':
                connections += 1
    return (connections <= 1)

def draw_whirlpool(corner: Corner, direction: Direction, h: int, w: int) -> list[str]:
    corn: str = TLC[corner]
    direc: str = TLD[direction]

    grid: list[list[str]] = [['.' for _ in range(w)] for _ in range(h)]

    # Get Starting Cell
    initial_pos: dict[str, tuple[int, int]] = {
        "TL": (0, 0),
        "TR": (0, w - 1),
        "BL": (h - 1, 0),
        "BR": (h - 1, w - 1)
    }
    pos: tuple[int, int] = initial_pos[corn]

    # Main Drawing Loop
    grid[pos[0]][pos[1]] = '#'
    direction_cycle: int = 0
    while direction_cycle < 5: # killswitch for when the whirlpool runs out of space
        direction_cycle += 1
        if valid_direction(grid, (pos[0] + DISTANCE[direc][0], pos[1] + DISTANCE[direc][1])):
            direction_cycle = 0
        # Draw as far as possible
        while valid_direction(grid, (pos[0] + DISTANCE[direc][0], pos[1] + DISTANCE[direc][1])):
            pos = (pos[0] + DISTANCE[direc][0], pos[1] + DISTANCE[direc][1])
            grid[pos[0]][pos[1]] = '#'
        # Change direction
        direc = ROTATE[direc]

    return [''.join(g) for g in grid]

