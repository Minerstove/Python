def sudapap(r,j,q=0):
    if j==0: return (q,r)
    return sudapap(j,r%j,q+r//j)