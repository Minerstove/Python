def matchups(n, names):
    def helper(remaining):
        if not remaining:
            return frozenset((frozenset(),))

        remaining = tuple(remaining)
        first = remaining[0]
        rest = remaining[1:]

        return frozenset(
            frozenset(submatching | frozenset(((first, partner),)))
            for i, partner in _enumerate(0, rest)
            for submatching in helper(rest[:i] + rest[i+1:])
        )

    return helper(names) 
        
def _enumerate(i, tuple):
    if len(tuple) == i:
        return ()
    
    return ((i, tuple[i]),) + _enumerate(i + 1, tuple)

assert matchups(2, ("Atienza", "Beltran", "Coronel", "Daryll")) == frozenset((
    frozenset((("Atienza", "Beltran"), ("Coronel", "Daryll"))),
    frozenset((("Atienza", "Coronel"), ("Beltran", "Daryll"))),
    frozenset((("Atienza", "Daryll"), ("Beltran", "Coronel"))),
)), matchups(2, ("Atienza", "Beltran", "Coronel", "Daryll"))
