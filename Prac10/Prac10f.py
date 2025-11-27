def warehouse_rearrange(n, q):
    n = list(range(n))
    for i, j in q:
        L = i
        R = j
        while L < R:
            swap1 = n[L]
            swap2 = n[R]
            n[L] = swap2
            n[R] = swap1
            L += 1
            R -= 1
    
    return n

assert warehouse_rearrange(7, (
    (2, 5),
    (1, 3),
    (3, 6),
    (4, 4),
    (3, 4),
)) == [0, 4, 5, 2, 6, 3, 1], warehouse_rearrange(7, (
    (2, 5),
    (1, 3),
    (3, 6),
    (4, 4),
    (3, 4),
))

