def proper_substring_pairs(strings):
    first_s = strings
    second_s = strings
    pairs = (
        (word2, word1) 
        for word1 in first_s 
        for word2 in second_s 
        if (word1 in word2 and word1 != word2)
    )

    return frozenset(pairs)


assert proper_substring_pairs((
    'dangerous', 'decoration', 'ration', 'ratio',
    'decor', 'rat', 'danger', 'anger', 'decorate',
)) == frozenset((
    ('decoration', 'rat'),
    ('decoration', 'ratio'),
    ('decoration', 'ration'),
    ('decoration', 'decor'),
    ('decorate', 'decor'),
    ('decorate', 'rat'),
    ('dangerous', 'danger'),
    ('dangerous', 'anger'),
    ('danger', 'anger'),
    ('ration', 'ratio'),
    ('ration', 'rat'),
    ('ratio', 'rat'),
)), proper_substring_pairs((
    'dangerous', 'decoration', 'ration', 'ratio',
    'decor', 'rat', 'danger', 'anger', 'decorate',
))

