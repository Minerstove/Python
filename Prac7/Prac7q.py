from itertools import count

def cf_denominators(k):
    p_0 = 1
    p_1 = k + 1 
    yield p_0
    yield p_1

    for a in count(k + 2):
        new_num = a*p_1 + p_0
        yield new_num
        p_1, p_0 = new_num, p_1

g = cf_denominators(1)

for i in range(10):
    print(next(g))