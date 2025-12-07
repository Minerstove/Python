def take_all_and_count(items, thing):
    thing = thing.lower()
    def f(items, thing, num_things, other_things):
        if not items:
            return (other_things, num_things)
        if items[0].lower() == thing:
            num_things = num_things + 1
        else:
            other_things = other_things + (items[0],)
        
        return f(items[1:], thing, num_things, other_things)
    
    return f(items, thing, 0, tuple())

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



        