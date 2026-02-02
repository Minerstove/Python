def merge(j, g):
    itj, itg = iter(j), iter(g)
    try:
        jimmy = next(itj)
    except StopIteration:
        for x in itg:
            yield x
        return
    try:
        gimmy = next(itg)
    except StopIteration:
        yield jimmy
        for x in itj:
            yield x
        return

    while True:
        if jimmy.lower() <= gimmy.lower():
            yield jimmy
            try:
                jimmy = next(itj)
            except StopIteration:
                yield gimmy
                for x in itg:
                    yield x
                return
        else:
            yield gimmy
            try:
                gimmy = next(itg)
            except StopIteration:
                yield jimmy
                for x in itj:
                    yield x
                return

                    

assert [*merge(
    ('Aerith', 'Barret', 'CaitSith', 'Cid', 'Cloud', 'Nanaki', 'Tifa', 'Vincent', 'Yuffie'),
    ('Amarant', 'Eiko', 'Freya', 'Garnet', 'Quina', 'Steiner', 'Vivi', 'Zidane'),
)] == [
    'Aerith', 'Amarant', 'Barret', 'CaitSith', 'Cid', 'Cloud', 'Eiko', 'Freya', 'Garnet',
    'Nanaki', 'Quina', 'Steiner', 'Tifa', 'Vincent', 'Vivi', 'Yuffie', 'Zidane',
], [*merge(
    ('Aerith', 'Barret', 'CaitSith', 'Cid', 'Cloud', 'Nanaki', 'Tifa', 'Vincent', 'Yuffie'),
    ('Amarant', 'Eiko', 'Freya', 'Garnet', 'Quina', 'Steiner', 'Vivi', 'Zidane'),
)]

assert [*merge(
    iter(('cid', 'CID', 'cId', 'cid', 'CID', 'cID', 'Cindy')),
    iter(('cid', 'cid', 'CID', 'cid', 'CiD', 'Cidney')),
)] == ['cid', 'CID', 'cId', 'cid', 'CID', 'cID', 'cid', 'cid', 'CID', 'cid', 'CiD', 'Cidney', 'Cindy'], [*merge(
    iter(('cid', 'CID', 'cId', 'cid', 'CID', 'cID', 'Cindy')),
    iter(('cid', 'cid', 'CID', 'cid', 'CiD', 'Cidney')),
)]


