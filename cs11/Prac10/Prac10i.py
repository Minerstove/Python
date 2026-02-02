def kth_strongest_chain(k, s):
    if k == 1:
        return max(s)
    

assert kth_strongest_chain(3, (4, 6, 6, 9, 2, 0, 1, 6)) == 6, kth_strongest_chain(3, (4, 6, 6, 9, 2, 0, 1, 6))
assert kth_strongest_chain(1, (4, 6, 6, 9, 2, 0, 1, 6)) == 9, kth_strongest_chain(1, (4, 6, 6, 9, 2, 0, 1, 6))
assert kth_strongest_chain(11, [4, 6, 6, 9, 2, 0, 1, 6]) == 4, kth_strongest_chain(11, [4, 6, 6, 9, 2, 0, 1, 6])
