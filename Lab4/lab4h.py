def in_and_out(bl, tr, people):
    x1, y1 = bl
    x2, y2 = tr
    inside, outside = [], []

    for name, (x,y) in people:
        if x1 < x < x2 and y1 < y < y2:
            inside.append(name)
        else:
            outside.append(name)
    
    return (inside, outside)

assert in_and_out((2, 2), (4, 4), [("Kevin", (1, 3)), ("Jem", (3, 3))]) == (["Jem"], ["Kevin"]), in_and_out((2, 2), (4, 4), [("Kevin", (1, 3)), ("Jem", (3, 3))])
