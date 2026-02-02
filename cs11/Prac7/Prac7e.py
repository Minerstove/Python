def all_subslices(iter_seq):
    tails = ()

    for x in iter_seq:
        yield (x,)

        for t in tails:
            yield t + (x, )
        
        tails = ((x,),) + tuple(t + (x,) for t in tails)

assert [*all_subslices((3, 1, 4, 1))] == [
    (3,),
    (1,),
    (3, 1),
    (4,),
    (1, 4),
    (3, 1, 4),
    (1,),
    (4, 1),
    (1, 4, 1),
    (3, 1, 4, 1),
], [*all_subslices((3, 1, 4, 1))]
print(*all_subslices((12,123,412,12,123)))