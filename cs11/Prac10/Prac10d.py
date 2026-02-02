def tekken_matchups(fighters):
    result = []
    counts = {}
    n = 0
    same_pairs = 0  # total of sum C(count[name], 2)

    for f in fighters:
        n += 1
        c = counts.get(f, 0)
        # When this fighter appears again, the number of same-name pairs increases by c
        same_pairs += c
        counts[f] = c + 1

        total_pairs = n * (n - 1) // 2
        result.append(total_pairs - same_pairs)

    return result

assert tekken_matchups((
    'Alisa', 'Panda', 'Alisa', 'Panda', 'Xiaoyu',
    'Julia', 'Panda', 'Panda', 'Panda', 'Panda',
    'Heihachi', 'Jinpachi', 'Panda', 'Azazel',
)) == [0, 1, 2, 4, 8, 13, 17, 21, 25, 29, 39, 50, 56, 69], tekken_matchups((
    'Alisa', 'Panda', 'Alisa', 'Panda', 'Xiaoyu',
    'Julia', 'Panda', 'Panda', 'Panda', 'Panda',
    'Heihachi', 'Jinpachi', 'Panda', 'Azazel',
))

# When getting a specific subset of a list, you can try getting all subsets of a list and subtracting the rest