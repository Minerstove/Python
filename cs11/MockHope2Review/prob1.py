def in_and_out(bl,tr,people):
    inside, outside = [], []

    def is_inside(x, y):
        blx, bly = bl
        trx, try_ = tr

        return blx <= x <= trx and bly <= y <= try_
    
    for name, (x,y) in people: #CAN DECOMPOSE VALUES LIKE THIS
        if is_inside(x,y):
            inside.append(name)
        else:
            outside.append(name)

    return (inside, outside)