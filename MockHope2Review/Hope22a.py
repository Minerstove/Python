def in_and_out(bl, tr, people):

    if not people:
        return ([],[])

    a, b = bl
    c, d = tr

    inside = []
    outside = []

    for name, coordinates, in people:
        x, y = coordinates
        if (a < x < c) and (b < y < d):
            inside.append(name)
        else:
            outside.append(name)

    return (inside, outside)
