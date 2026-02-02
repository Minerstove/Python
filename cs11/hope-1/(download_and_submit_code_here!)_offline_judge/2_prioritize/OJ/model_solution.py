def compare(tup1,tup2):
    if tup1 == (): return tup2
    (n1,d1,f1,i1),(n2,d2,f2,i2) = tup1,tup2
    return tup1 if (-d2,f2,-len(n2),i2) < (-d1,f1,-len(n1),i1) else tup2
def prioritize(s):
    best = ()
    #this comprehension goes through each element and replaces best if it is better
    tuple(best := compare(best,tupn) for tupn in s) 
    return best[0]