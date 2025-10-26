def battle_tictactoe_scores(grid):
    r, c = len(grid), len(grid[0])
    k = y = 0

    def counter(s):
        k_add = y_add = 0
        for i in range(len(s) - 3):
            w = s[i:i + 4]
            if w == "KKKK":
                k_add += 1
            elif w == "YYYY":
                y_add += 1
        return k_add, y_add

    # rows
    for row in grid:
        dk, dy = counter(row)
        k += dk; y += dy

    # columns (transpose with zip)
    for col in zip(*grid):
        dk, dy = counter("".join(col))
        k += dk; y += dy

    # diagonals: top-left -> bottom-right
    # offsets d = j - i
    for d in range(-(r - 1), c):
        diag = "".join(grid[i][i + d] for i in range(max(0, -d), min(r, c - d)))
        if len(diag) >= 4:
            dk, dy = counter(diag)
            k += dk; y += dy

    # diagonals: top-right -> bottom-left
    # sums s = i + j
    for s in range(r + c - 1):
        diag = "".join(
            grid[i][s - i]
            for i in range(max(0, s - (c - 1)), min(r, s + 1))
            if 0 <= s - i < c
        )
        if len(diag) >= 4:
            dk, dy = counter(diag)
            k += dk; y += dy

    return (k, y)


assert battle_tictactoe_scores((
    'KKKKKKY',
    'YKYKYKY',
    'KYKYKYY',
    'YYYKKKY',
    'YYYKKKY',
)) == (6, 3), battle_tictactoe_scores((
    'KKKKKKY',
    'YKYKYKY',
    'KYKYKYY',
    'YYYKKKY',
    'YYYKKKY',
))


