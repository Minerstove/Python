def num_subarrays(a, p):
    result = 0
    n = len(a)
    prod = 1
    L = 0

    for R in range(n):
        prod *= a[R]
        while prod > p and L <= R:
            prod //= a[L]
            L += 1

        result += R - L + 1


    return result
