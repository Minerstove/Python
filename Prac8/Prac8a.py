def game_mistakes(words, used):
    wordset = set(words)
    seen = set()
    a = b = 0  # A plays even indices, B plays odd indices

    for i, w in enumerate(used):
        bad = False

        # rule 1: must be in dictionary
        if w not in wordset:
            bad = True

        # rule 2: must chain from previous word
        if i > 0 and used[i-1][-1] != w[0]:
            bad = True

        # rule 3: no repeats
        if w in seen:
            bad = True

        if bad:
            if i % 2 == 0:
                a += 1
            else:
                b += 1

        seen.add(w)

    return (a, b)



assert game_mistakes((
    'porkchop', 'kanin', 'ketchup', 'chopsuey', 'bulalo', 'adobo',
    'chicken', 'mami', 'longsilog', 'tocilog', 'tapsi', 'pancit',
    'lugaw', 'lomi', 'tokwatbaboy', 'paresbeef', 'friedsiomai',
    'siopao', 'burger', 'avocado', 'gulaman', 'apple', 'spaghetti',
    'taho', 'nut', 'croissant', 'linguine', 'pineapple', 'kutsinta',
    'edamame', 'hazelnut', 'yema', 'tinapay', 'durian', 'pizza',
    'orange', 'iodizedsalt', 'tea', 'eggplant', 'puto', 'legumes',
    'oatmeal', 'noodles', 'tofu', 'nutella', 'egg', 'udon', 'sago',
), (
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
)) == (5, 3), game_mistakes((
    'porkchop', 'kanin', 'ketchup', 'chopsuey', 'bulalo', 'adobo',
    'chicken', 'mami', 'longsilog', 'tocilog', 'tapsi', 'pancit',
    'lugaw', 'lomi', 'tokwatbaboy', 'paresbeef', 'friedsiomai',
    'siopao', 'burger', 'avocado', 'gulaman', 'apple', 'spaghetti',
    'taho', 'nut', 'croissant', 'linguine', 'pineapple', 'kutsinta',
    'edamame', 'hazelnut', 'yema', 'tinapay', 'durian', 'pizza',
    'orange', 'iodizedsalt', 'tea', 'eggplant', 'puto', 'legumes',
    'oatmeal', 'noodles', 'tofu', 'nutella', 'egg', 'udon', 'sago',
), (
    'pizza', 'apple', 'egg', 'hazelnut', 'tofu', 'udon', 'nut',
    'tinapay', 'yema', 'edamame', 'eggplant', 'durian', 'nutella',
    'avocado', 'orangutan', 'noodles', 'spaghetti', 'iodizedsalt',
    'toatmeal', 'linguine', 'egg', 'gulaman', 'nut', 'tea', 'uh',
))


