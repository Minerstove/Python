def total_excitement(players):
    for i in players:
        others = players[:i] + players[i + 1:]

assert total_excitement((3, 1, 4, 1)) == 8, total_excitement((3, 1, 4, 1))
