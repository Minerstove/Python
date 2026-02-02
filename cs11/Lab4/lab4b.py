def enemy_lists(names, enemy_pairs):
    burnbook = {}

    #initalizing dictionary
    for name in names:
        burnbook[name] = set()

    for x, y in enemy_pairs:
        burnbook[x].add(y)
        burnbook[y].add(x)

    return {k: sorted(list(burnbook[k])) for k in sorted(burnbook)}

assert enemy_lists({
    'ange', 'battler', 'erika', 'eva', 'genji', 'george',
    'hideyoshi', 'jessica', 'kanon', 'krauss', 'kyrie',
    'maria', 'natsuhi', 'rosa', 'rudolf', 'shannon',
}, [
    ('jessica', 'krauss'),
    ('rudolf', 'kyrie'),
    ('ange', 'battler'),
    ('eva', 'george'),
    ('eva', 'hideyoshi'),
    ('krauss', 'natsuhi'),
    ('kyrie', 'ange'),
    ('george', 'eva'),
    ('rosa', 'maria'),
    ('jessica', 'natsuhi'),
    ('eva', 'george'),
]) == {
    'ange': ['battler', 'kyrie'],
    'battler': ['ange'],
    'erika': [],
    'eva': ['george', 'hideyoshi'],
    'genji': [],
    'george': ['eva'],
    'hideyoshi': ['eva'],
    'jessica': ['krauss', 'natsuhi'],
    'kanon': [],
    'krauss': ['jessica', 'natsuhi'],
    'kyrie': ['ange', 'rudolf'],
    'maria': ['rosa'],
    'natsuhi': ['jessica', 'krauss'],
    'rosa': ['maria'],
    'rudolf': ['kyrie'],
    'shannon': [],
}, enemy_lists({
    'ange', 'battler', 'erika', 'eva', 'genji', 'george',
    'hideyoshi', 'jessica', 'kanon', 'krauss', 'kyrie',
    'maria', 'natsuhi', 'rosa', 'rudolf', 'shannon',
}, [
    ('jessica', 'krauss'),
    ('rudolf', 'kyrie'),
    ('ange', 'battler'),
    ('eva', 'george'),
    ('eva', 'hideyoshi'),
    ('krauss', 'natsuhi'),
    ('kyrie', 'ange'),
    ('george', 'eva'),
    ('rosa', 'maria'),
    ('jessica', 'natsuhi'),
    ('eva', 'george'),
])



