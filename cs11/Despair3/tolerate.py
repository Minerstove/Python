R, C, Q, T = map(int, input().split())

grid = []
for r in range(R):
    grid.append(list(input().strip()))

for q in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    taylor = 0
    olivia = 0

    top    = min(r1, r2)
    bottom = max(r1, r2)
    left   = min(c1, c2)
    right  = max(c1, c2)

    taylor = 0
    olivia = 0

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] == "T":
                taylor += 1
            elif grid[i][j] == "O":
                olivia += 1

    if taylor - olivia <= T:
        print("good 4 u")
    else:
        print("bad idea, right")
