def billy_movement(r,c,s):
    grid = [["." for _ in range(c)] for _ in range(r)]
    s_row, s_col = 0, 0
    dr, dc = 1, 1

    for _ in range(s + 1):
        grid[s_row][s_col] = "*"
        nr, nc = s_row + dr, s_col + dc

        if nr < 0 or nr >= r:
            dr *= -1
            nr = s_row + dr

        if nc < 0 or nc >= c:
            dc *= -1
            nc = s_col + dc

        s_row, s_col = nr, nc
    
    for row in grid:
        print("".join(row))

billy_movement(4, 6, 6)
print("\n")
billy_movement(3, 5, 20)
print("\n")
billy_movement(3, 6, 20)




