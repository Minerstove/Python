def max_happiness(a, b, c):
    n = len(a)

    study = [None] * n
    chores = [None] * n
    friends = [None] * n

    study[0] = a[0]
    chores[0] = b[0]
    friends[0] = c[0]

    for i in range(1, n):
        study[i] = max(study[i - 1], chores[i - 1], friends[i - 1]) + a[i]
        chores[i] = max(study[i - 1], chores[i - 1], friends[i - 1]) + b[i]
        friends[i] = max(study[i - 1], chores[i - 1]) + c[i]

    return max(study[n - 1], chores[n - 1], friends[n - 1])

assert max_happiness([1, 1, 1, 11], [10, 10, 10, 11], [100, 100, 100, 11]) == 221, max_happiness([1, 1, 1, 11], [10, 10, 10, 11], [100, 100, 100, 11])
