def take_all_and_count(store_items,item):
    def helper(store_items, item, counter, remaining_items):
        if len(store_items) == 0:
            return (remaining_items,) + (counter, )
        first, rest = store_items[0], store_items[1:]
        if first.lower() == item.lower():
            return helper(rest, item, counter + 1, remaining_items)
        else:
            remaining_items = remaining_items + (first, )
            return helper(rest, item, counter, remaining_items)
    
    return helper(store_items, item, 0, ())

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