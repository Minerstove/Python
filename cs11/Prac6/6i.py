def move2d(loc, moves):
    l_loc = list(loc)
    for direc, step in moves:
        if direc == "south":
            l_loc[1] -= step
        elif direc == "west":
            l_loc[0] -= step
        elif direc == "north":
            l_loc[1] += step
        else:
            l_loc[0] += step

    return tuple(l_loc)

assert move2d((3, 5), (
    ('south', 2),
    ('east', 5),
    ('west', 3),
    ('south', 2),
    ('south', 5),
)) == (5, -4), move2d((3, 5), (
    ('south', 2),
    ('east', 5),
    ('west', 3),
    ('south', 2),
    ('south', 5),
))

