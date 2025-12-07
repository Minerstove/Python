def possible_sums(*args):
    if len(args) == 1:
        return frozenset((args[0], -args[0]))
    s = sum(args)
    n = len(args)
    result = frozenset(s - 2*args[i] for i in range(n)) | frozenset((sum(args),))
    return result

assert possible_sums(1, 2, 3) == frozenset((6, 4, 2, 0)), possible_sums(1, 2, 3)

