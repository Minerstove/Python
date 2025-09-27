def take_all_and_count(store_items,item):
    num_of_items = len(tuple(thing for thing in store_items if thing.lower() == item.lower()))
    return (tuple(thing for thing in store_items if thing.lower() != item.lower()),) + (num_of_items,)

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

#DONE



