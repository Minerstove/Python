def mkns_2(M,ML,TL,MI):
    if len(M)!=len(set(M)): return "No test cases"
    ML_f = frozenset(ML)
    TL_f = frozenset(TL)
    MI_f = frozenset(MI)

    delulu = tuple(i for i in M if i in ML_f and i in TL_f)
    may_chance = tuple(i for i in M if i in TL_f and i in MI_f)
    wag_red_flag = tuple(i for i in M if i in ML_f and i in MI_f)

    return delulu, may_chance, wag_red_flag