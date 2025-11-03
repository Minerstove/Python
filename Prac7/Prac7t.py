def spiral_coords():
    x, y = 0, 0
    yield (x, y)

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    di = 0

    length = 1
    while True:
        for _ in range(2):
            dx, dy = dirs[di]
            for _ in range(length):
                x = x + dx
                y = y + dy
                yield (y, x)
            di = (di + 1) % 4
        length += 1

g = spiral_coords()
for _ in range(10):
    print(next(g))
