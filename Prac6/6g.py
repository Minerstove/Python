def flower_heights(flowers, ranges):
    n = len(flowers)
    diff = [0] * (n + 1)
    
    l_flowers = list(flowers)

    for i, j in ranges:
        diff[i - 1] += 2
        diff[j] -= 2

    running = 0
    for k in range(n):
        running += diff[k]
        l_flowers[k] += running

    return l_flowers

assert flower_heights((3, 1, 4, 1, 5), (
        (1, 4),
        (3, 5),
        (4, 4),
    )) == [5, 3, 8, 7, 7], flower_heights((3, 1, 4, 1, 5), (
        (1, 4),
        (3, 5),
        (4, 4),
    ))


