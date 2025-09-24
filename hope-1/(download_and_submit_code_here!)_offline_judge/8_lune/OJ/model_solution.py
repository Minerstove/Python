def lune(l):
    if l == 0:
        return ()
    tiers = "ABSU"
    
    def tier_from_streak(streak):
        if streak >= 10: return 'U'
        if streak >= 5:  return 'S'
        if streak >= 2:  return 'B'
        return 'A'
    def drop_streak(streak):
        if streak >= 10: return 5
        if streak >= 5:  return 2
        if streak >= 2:  return 0
        return 0
    def gen(pos, streak, s):
        if pos == l:
            return (s,)
        out = ()
        
        #multiplier for this position depends on current streak
        tier = tier_from_streak(streak)
        # hit: streak increases
        out += gen(pos + 1, streak + 1, s + tier)
        # miss: streak drops down
        out += gen(pos + 1, drop_streak(streak), s + tier)

        return out

    return frozenset(gen(0, 0, ""))