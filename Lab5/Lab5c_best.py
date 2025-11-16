def num_subarrays(a, p):
    prod = 1
    left = 0
    total = 0

    for right, x in enumerate(a):
        prod *= x
        while prod > p and left <= right:
            prod //= a[left]
            left += 1
        total += right - left + 1
    return total

assert num_subarrays((2, 1, 2), 3) == 5, num_subarrays((2, 1, 2), 3)
