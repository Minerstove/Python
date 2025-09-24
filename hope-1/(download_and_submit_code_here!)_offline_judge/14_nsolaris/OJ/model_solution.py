def gcd(a,b):
  if a==0: return b 
  return gcd(b%a,a)
  
def lcm(a,b):
    return a*b//gcd(a,b)

# def nsolaris(tup,M,N):
#     if len(tup)==1:
#         a=tup[0]
#         return N//a-(M-1)//a

#     elif len(tup)==2:
#         a,b=tup
#         ab=lcm(a,b)
#         return (N//a+N//b-N//ab)-((M-1)//a+(M-1)//b-(M-1)//ab)

#     elif len(tup)==3:
#         a,b,c=tup
#         ab=lcm(a,b)
#         ac=lcm(a,c)
#         bc=lcm(b,c)
#         abc=lcm(ab,c)
#         return (N//a+N//b+N//c-N//ab-N//ac-N//bc+N//abc)-((M-1)//a+(M-1)//b+(M-1)//c-(M-1)//ab-(M-1)//ac-(M-1)//bc+(M-1)//abc)

#HEARTBREAK
def nsolaris(tup,M,N):
    n=len(tup)
    total=0
    
    for mask in range(1,1<<n): 
        bits=[tup[i] for i in range(n) if mask & (1<<i)]
        l=bits[0]
        for x in bits[1:]:
            l=lcm(l,x)
        sign = (-1)**(len(bits)+1)
        total += sign*(N//l - (M-1)//l)
    return total
