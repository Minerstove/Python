from itertools import count

def cf_numerators(k):
    p_0 = k
    p_1 = k*(k+1) + 1
    yield p_0
    yield p_1

    for a in count(k + 2):
        new_num = a*p_1 + p_0
        yield new_num
        p_1, p_0 = new_num, p_1

g = cf_numerators(1)

for i in range(10):
    print(next(g))
