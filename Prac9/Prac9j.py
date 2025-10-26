def sorted_streaks(ints):
    if not ints:
        return []
    result = []
    start = ints[0]

    window = [start,]
    for i in range(1, len(ints)):
        if start > ints[i]:
            result.append(tuple(window))
            window = [ints[i],]
            start = ints[i]
        else:
            window.append(ints[i])
            start = ints[i]

    result.append(tuple(window))
    return result

assert sorted_streaks((3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 3)) == [
    (3,),
    (1, 4),
    (1, 5, 9),
    (2, 6),
    (5,),
    (3, 5, 8, 9),
    (7, 9),
    (3, 3),
],sorted_streaks((3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 3))