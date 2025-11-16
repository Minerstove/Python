def num_subarrays(a, p):
    n = len(a)
    result = 0

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= a[j]
            if prod <= p:
                result += 1
            else:
                break
    return result

assert num_subarrays((2, 1, 2), 3) == 5, num_subarrays((2, 1, 2), 3)
