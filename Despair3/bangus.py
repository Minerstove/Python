R, C = map(int, input().split())

grid = [input() for _ in range(R)]

fish = [
    "  ;,//;,    ,;/",
    " o:::::::;;///",
    ">::::::::;;\\\\\\",
    "  ''\\\\\\\\'\"  ';\\",
]

n = len(fish)
w = max(len(row) for row in fish)

pattern_cells = []
for r in range(n):
    for c in range(len(fish[r])):
        ch = fish[r][c]
        if ch != ' ':
            pattern_cells.append((r, c, ch))

count = 0

for sr in range(R - n + 1):      # starting row
    for sc in range(C - w + 1):  # starting column
        ok = True
        for dr, dc, ch in pattern_cells:
            rr = sr + dr
            cc = sc + dc

            # If grid line is too short, treat as mismatch
            if cc >= len(grid[rr]) or grid[rr][cc] != ch:
                ok = False
                break

        if ok:
            count += 1

print(count)