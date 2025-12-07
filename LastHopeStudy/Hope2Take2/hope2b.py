def passes_vibe_check(ratings):

    d = {}
    for vibe in ratings:
        d[vibe] = d.get(vibe, 0) + 1

    max_freq = max(d.values())
    count_max = sum(1 for x in d.values() if x == max_freq)

    return count_max == 2

assert passes_vibe_check([10, 0, 0, 10, 1]) == True, passes_vibe_check([10, 0, 0, 10, 1])
assert passes_vibe_check([1000, 9, 7, 8, 1000, 8, 7]) == False, passes_vibe_check([1000, 9, 7, 8, 1000, 8, 7])

