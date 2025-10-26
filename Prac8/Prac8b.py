def battle_tictactoe_scores(grid):
    r = len(grid)
    c = len(grid[0])

    k, y = 0, 0
    #Check rows
    for row in grid:
        checker = row[0]
        for char in row:
            if char == checker[-1]:
                checker += char
            else:
                if checker == "KKKK":
                    k += 1
                elif checker == "YYYY":
                    y += 1


    #Check Columns

    
    #Check Diagonals