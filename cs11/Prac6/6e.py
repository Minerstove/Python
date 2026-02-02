def find_good_pen(pens, p1, p2, r1, r2):
    n = len(pens)
    good_pens = []

    for i in range(n):
        pen, price, rating = pens[i][0], pens[i][1], pens[i][2]
        if price in range(p1, p2 + 1):
            if rating in range(r1, r2 + 1):
                good_pens.append(pen)

    return good_pens


assert find_good_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 20, 888, 6, 9) == [
    'Black Ballpen',
    'Blue Ballpen',
    'Sign Pen',
    'Pencil',
], find_good_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 20, 888, 6, 9)



