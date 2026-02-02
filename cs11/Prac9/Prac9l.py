def total_excitement(players):
    n = len(players)
    result = 0

    for i in range(n):
        x = players[i]
        for j in range(i + 1, n):
            y = players[j]
            if (x * y) % 2 == 1:
                result += (x * y)
            else:
                result += (x*y + x + y + 1)
        
    return result

assert total_excitement([3, 1, 4]) == 33, total_excitement([3, 1, 4])