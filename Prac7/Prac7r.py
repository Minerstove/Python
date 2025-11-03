from itertools import count
from fractions import Fraction

def convergents(k):
    p_0 = k
    p_1 = k*(k+1) + 1

    q_0 = 1
    q_1 = k + 1 

    yield Fraction(p_0, q_0)
    yield Fraction(p_1, q_1)
    
    for a in count(k + 2):
        new_num = a*p_1 + p_0
        new_denom = a*q_1 + q_0
        yield Fraction(new_num, new_denom)
        p_1, p_0 = new_num, p_1
        q_1, q_0 = new_denom, q_1

g = convergents(1)

for i in range(10):
    print(next(g))