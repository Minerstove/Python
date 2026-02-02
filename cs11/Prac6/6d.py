def find_pen(pens, buy):
    n = len(pens)

    for i in range(n):
        pen, price, rating = pens[i][0], pens[i][1], pens[i][2]
        if pen == buy:
            return (price, rating)
    
    raise ValueError

assert find_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 'Pencil') == (800, 7), find_pen((
    ('Black Ballpen', 20, 8),
    ('Blue Ballpen', 20, 8),
    ('White Ballpen', 50, 1),
    ('Sign Pen', 100, 9),
    ('Pencil', 800, 7),
    ('Fountain Pen', 20, 2),
    ('Waifu Pen', 5000, 10),
), 'Pencil')

