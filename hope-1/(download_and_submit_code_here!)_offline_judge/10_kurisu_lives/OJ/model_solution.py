def k_comb(tup, k): #combinations, fast for this problem (how many ways to choose k elements from tup where order doesn't matter)
    if k==0: return ((),) 
    if tup==(): return ()
    return tuple(
        (tup[0], *rest)
        for rest in k_comb(tup[1:],k-1) #branch where tup[0] is included
    ) + k_comb(tup[1:],k) #branch where tup[0] isn't included

# print(k_comb((2,)*10,5))

def kurisu_lives(tl,k,n):
    arr = tuple(sum(tup) for tup in k_comb(tl,k))
    if n in arr: return 'Convergence'
    return 'Divergence'
    ...