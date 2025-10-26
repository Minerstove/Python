def jeepney_groups(passengers, jeepney_counts):
    it_pas = iter(passengers)
    it_jeep = iter(jeepney_counts)
    for x in it_jeep:
        try:
            first =  next(it_pas)
        except StopIteration:
            return

        jeep = (first,)
        for _ in range(x - 1):
            try:
                jeep += (next(it_pas),)
            except StopIteration:
                yield jeep
                return
        yield jeep

assert [*jeepney_groups(
    iter(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina')),
    iter((3, 4, 1)),
)] == [
    ('eiko', 'dagger', 'freya'),
    ('amarant', 'vivi', 'steiner', 'zidane'),
    ('quina',),
], [*jeepney_groups(
    iter(('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina')),
    iter((3, 4, 1)),
)]

assert [*jeepney_groups(
    ('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'),
    (3, 4, 20),
)] == [
    ('eiko', 'dagger', 'freya'),
    ('amarant', 'vivi', 'steiner', 'zidane'),
    ('quina',),
], [*jeepney_groups(
    ('eiko', 'dagger', 'freya', 'amarant', 'vivi', 'steiner', 'zidane', 'quina'),
    (3, 4, 20),
)]

