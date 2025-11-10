def movie_count(mins,cost,b1,b2):
    s_cost = sorted(cost)
    result = 0

    for m in mins:

        L = ceil_div(b1, 60 * m)
        U = floor_div(b2, 60 * m)
        if L > U:
            continue
        i = lower_bound(s_cost, L)
        j = upper_bound(s_cost, U)
        result += (j - i)

    return result


def lower_bound(things, bound):
    lo, hi = 0, len(things)
    while lo < hi:
        mid = (lo + hi) // 2
        if things[mid] < bound:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(things, bound):
    lo, hi = 0, len(things)
    while lo < hi:
        mid = (lo + hi) // 2
        if things[mid] <= bound:
            lo = mid + 1
        else:
            hi = mid
    return lo

def ceil_div(a, b):
    return -(-a // b)

def floor_div(a, b):
    return a // b

assert movie_count(
    [90, 63, 120, 70, 150],
    (3, 1, 4, 9, 6),
    5_000,
    15_000
) == 5, movie_count(
    [90, 63, 120, 70, 150],
    (3, 1, 4, 9, 6),
    5_000,
    15_000
)
