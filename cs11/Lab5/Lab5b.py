def movie_count(mins,cost,b1,b2):
    result = 0
    for minute in mins:
        for actor in cost:
            total = minute*60*actor
            if b1 <= total <= b2:
                result += 1
    
    return result

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

