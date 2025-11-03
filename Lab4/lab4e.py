def bomb_records(bs, p):
    bomb_record = {}

    for bi, bj in bs:
        for dx in range(-p, p + 1):
            if p == abs(dx):
                dy_values = (p - abs(dx),)
            else:
                dy_values = (-(p - abs(dx)), p - abs(dx))

            for dy in dy_values:
                bomb_record[(bi, bj)] = bomb_record.get((bi,bj), set())
                bomb_record[(bi, bj)].add((bi + dx, bj + dy))

    return bomb_record

assert bomb_records(((0, 0), (1, 1)), 1) == {
    (0, 0): {(-1, 0), (1, 0), (0, 1), (0, -1)},
    (1, 1): {(0, 1), (2, 1), (1, 0), (1, 2)},
}, bomb_records(((0, 0), (1, 1)), 1)