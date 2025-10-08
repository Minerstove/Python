def game_mistakes(names):
    n = len(names)
    a = 0
    b = 0
    for i in range(n - 1):
        lchar, fchar = names[i][-1], names[i + 1][0]
        if lchar != fchar:
            if i % 2 == 0:
                b += 1
            else:
                a += 1

    return (a, b)


assert game_mistakes((
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
)) == (1, 3), game_mistakes((
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
))

