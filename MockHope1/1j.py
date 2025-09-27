def proper_substring_pairs(strings):
    if not strings:
        return frozenset()
    if len(strings) == 1:
        return frozenset()
    
    return frozenset(
        (strings[i], strings[j])
        for i in range(len(strings))
        for j in range(len(strings))
        if i != j 
        and strings[j] in strings[i]
        and len(strings[j]) < len(strings[i])
    )

print(proper_substring_pairs("string"))
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


