def divisible_by_exactly_one(x, y, u, v):
    for i in range(x, y + 1):
        if (i % u == 0) ^ (i % v == 0):
            print(i)

divisible_by_exactly_one(10, 20, 3, 5)

