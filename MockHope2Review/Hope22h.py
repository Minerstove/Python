def redraw_maze_in_a_nice_way(grid):
    r, c = len(grid), len(grid[0])
    
    def wall(i, j):
        return 0 <= i < r and 0 <= j < c and grid[i][j] == '#'

    for i in range(r):
        line = ""
        for j in range(c):
            if grid[i][j] != '#':
                line += " "
                continue

            # Check for neighboring walls
            up    = wall(i - 1, j)
            down  = wall(i + 1, j)
            left  = wall(i, j - 1)
            right = wall(i, j + 1)

            # Pick character by pattern
            if up and down and left and right:
                ch = "┼"
            elif up and down and left:
                ch = "┤"
            elif up and down and right:
                ch = "├"
            elif left and right and up:
                ch = "┴"
            elif left and right and down:
                ch = "┬"
            elif up and down:
                ch = "│"
            elif left and right:
                ch = "─"
            elif up and left:
                ch = "╯"
            elif up and right:
                ch = "╰"
            elif down and left:
                ch = "╮"
            elif down and right:
                ch = "╭"
            elif up:
                ch = "╵"
            elif down:
                ch = "╷"
            elif left:
                ch = "╴"
            elif right:
                ch = "╶"
            else:
                ch = " "
            
            line += ch
        print(line.rstrip())

redraw_maze_in_a_nice_way((
    "#################",
    "#   #   #       #",
    "### ### ### #####",
    "#   # #         #",
    "# ### # # #######",
    "# # # # #       #",
    "# # # ### #######",
    "# # # # # #     #",
    "# # # # # # #####",
    "# #     # #     #",
    "# ### # # # ### #",
    "#     #       # #",
    "#################",
))
