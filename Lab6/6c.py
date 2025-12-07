def movie_count(movies, actors, b1, b2):
    result = []
    actors = sorted(actors)
    for movie in movies:
        result.append(upper_bound(actors, b2, movie) - lower_bound(actors, b1, movie))

    return sum(result)

def lower_bound(actors, b1, movie):
    lo, hi = 0, len(actors)
    value = -((-b1)//(60*movie))
    while lo < hi:
        mid = (lo + hi) // 2
        if actors[mid] >= value:
            hi = mid
        else:
            lo = mid + 1

    return lo


def upper_bound(actors, b2, movie):
    lo, hi = 0, len(actors)
    value = b2//(60*movie)
    while lo < hi:
        mid = (lo + hi) // 2
        if actors[mid] > value:
            hi = mid
        else:
            lo = mid + 1

    return lo


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

