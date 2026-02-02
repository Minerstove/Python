def take_all_and_count(items, thing):
    new_items = tuple(item for item in items if item.lower() != thing.lower())
    numthings = sum(1 for item in items if item.lower() == thing.lower())

    return (new_items, numthings)

assert take_all_and_count(
    ('ramen', 'ramyun', 'lomein', 'ramen', 'ramyun', 'lomein'),
    'ramen',
) == (('ramyun', 'lomein', 'ramyun', 'lomein'), 2), take_all_and_count(
    ('ramen', 'ramyun', 'lomein', 'ramen', 'ramyun', 'lomein'),
    'ramen',
)

assert take_all_and_count(
    ('Bag', 'earrings', 'rings', "EarRings", 'kaban', 'ramen', 'EARRINGS', 'eArRiNgS', 'RAMEN', 'ears'),
    'Earrings',
) == (('Bag', 'rings', 'kaban', 'ramen', 'RAMEN', 'ears'), 4), take_all_and_count(
    ('Bag', 'earrings', 'rings', "EarRings", 'kaban', 'ramen', 'EARRINGS', 'eArRiNgS', 'RAMEN', 'ears'),
    'Earrings',
)