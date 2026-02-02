def optimal_matchups(players):
    s = sorted(players)
    n = len(s)
    if n < 2:
        return 0

    if n % 2 == 0:
        return sum(s[i+1] - s[i] for i in range(0, n, 2))
    
    best = 10**18
    for skip in range(n):
        arr = [s[i] for i in range(n) if i != skip]
        total = sum(arr[i+1] - arr[i] for i in range(0, len(arr), 2))
        best = min(best, total)
    return best


assert optimal_matchups((1, 7, 2, 10, 4, 7)) == 7, optimal_matchups((1, 7, 2, 10, 4, 7))
assert optimal_matchups([3, 1, 4]) == 1, optimal_matchups([3, 1, 4])

# Still gotta do the hard case. Mainly for when n is odd. Build a stage so instead of reloading the whole list every time we skip, you can skip per thing