def convert(d0, d1, d2, b):
    return d0+b*(d1+d2*b)

def packs_to_buy(a, b):
    return -(-a//b)

def total_legs(h, w, p):
    return h*2+(w+p)*4

def num_subsquares(n, k):
    return (n-k+1)*2

def pow_digits(a, b):
    return str(pow(a, b,10**11)).zfill(11) #fills digits with zero up the the parameter

def cards_to_give(a, b):
    return a//b

def perimeter(h, w):
    return 2*(h+w)

from fractions import Fraction

def substitute(a, b):
    return Fraction((a+b+a*b+3)/((a+1)*b+1)*3)

def number_head(n):
    return int(str(n)[0])

def number_tail(n):
    return (int(str(abs(n))[:-1]) if str(abs(n))[:-1] else None,
            int(str(abs(n))[-1])  if str(abs(n))[-1:]  else None) #(int(str(n[0::(len(str(n))-1)])),int(str(n[-1])))

print(number_tail(123))
print(number_tail(5))

def largest_bitonic_at_most(n):
    def is_bitonic(num_str):
        i = 1
        while i < len(num_str) and num_str[i] >= num_str[i-1]:
            i += 1
        while i < len(num_str) and num_str[i] <= num_str[i-1]:
            i += 1
        return i == len(num_str)

    def construct_bitonic(n):
        digits = list(map(int, str(n)))
        length = len(digits)
        result = digits[:]
        state = "UP"

        for i in range(1, length):
            if state == "UP":
                if result[i] < result[i-1]:
                    state = "DOWN"
                    result[i] = min(result[i], result[i-1])
            else:  
                if result[i] > result[i-1]:
                    result[i] = result[i-1]

        while int("".join(map(str, result))) > n or not is_bitonic("".join(map(str, result))):
            i = length - 1
            while i >= 0 and result[i] == 0:
                result[i] = 9
                i -= 1
            if i >= 0:
                result[i] -= 1
                for j in range(i+1, length):
                    result[j] = 9

        return int("".join(map(str, result)))

    if __name__ == "__main__":
        print("Largest bitonic ≤", n, "is", construct_bitonic(n))
print(largest_bitonic_at_most(2998))
print(largest_bitonic_at_most(202))

def construct_bitonic(n):
    s=str(n); L=len(s)
    def F(p,prev,down,t):
        if p==L: return ''
        st=int(s[p]) if t else 9
        def G(d,prev,down,t):
            if d<0: return None
            if prev<0:
                ok=True; nd=down
            elif not down:
                ok=True; nd=down or d<prev
            else:
                ok=d<=prev; nd=True
            if ok:
                suf=F(p+1,d,nd,t and d==st)
                if suf is not None: return str(d)+suf
            return G(d-1,prev,down,t and d==st)
        return G(st,prev,down,t)
    r=F(0,-1,False,True)
    return int(r.lstrip('0') or '0')

print(construct_bitonic(2998))
print(construct_bitonic(202))