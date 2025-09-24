def rotate_cw(pos, r, c): return (c-1-pos[1], pos[0])
def rotate_ccw(pos, r, c): return (pos[1], r-1-pos[0])
def rotate_180(pos, r, c): return rotate_cw(rotate_cw(pos, r, c),r,c)
def flip_main(pos, r, c): return (pos[1], pos[0])
def flip_anti(pos, r, c): return (c-1-pos[1], r-1-pos[0])

def parse_gauntlet(gauntlet):
    ops = tuple(
        (int(''.join(ch for ch in chunk if ch.isdigit())),
         ''.join(ch for ch in chunk if ch.isalpha()))
        for chunk in gauntlet.split('.')
    )
    
    def apply_tt_rec(ops, history=()):
        if not ops:
            return history
        cnt, op = ops[0]
        if op == 'TT':
            def reduce_history(hist, remaining):
                if not hist or remaining == 0:
                    return hist
                k, o = hist[-1]
                if remaining < k:
                    return hist[:-1] + ((k - remaining, o),)
                else:
                    return reduce_history(hist[:-1], remaining - k)
            return apply_tt_rec(ops[1:], reduce_history(history, cnt))
        else:
            return apply_tt_rec(ops[1:], history + ((cnt, op),))
    
    history = apply_tt_rec(ops)
    
    mods_key = ('CW','CCW','F','FL','FR')
    mods_val = (4,4,2,2,2)
    history = tuple((k%mods_val[mods_key.index(op)],op) for (k,op) in history)
    
    return history

    
def sugar_rush_villain(grid, gauntlet):
    r, c = len(grid), len(grid[0])
    ops = parse_gauntlet(gauntlet)
    # print(ops)
    
    transf_keys = ('CW','CCW','F','FL','FR')
    transf_funcs = (rotate_cw, rotate_ccw, rotate_180, flip_main, flip_anti)

    def net_trans(pos, ops_index=0, repeat_index=0):
        if ops_index >= len(ops):
            return pos

        k, t = ops[ops_index]
        func = transf_funcs[transf_keys.index(t)]

        if repeat_index < k:
            return net_trans(func(pos, r, c), ops_index, repeat_index + 1)
        else:
            return net_trans(pos, ops_index + 1, 0)
    return tuple(
        "".join(grid[i][j] for i,j in (net_trans((i,j)) for j in range(c)))
        for i in range(r)
    )
