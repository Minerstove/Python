def ltn(l): #letter to num
    l=l.upper()
    return (ord(l)-ord('A')+1)

def ntl(n): #num to letter
    return chr((ord('A')+(n-1)%26))

def keep_punc(s_old,s_new,o=0,d=0):
    if o==len(s_old): return ""
    if not s_old[o].isalpha():
        return s_old[o]+keep_punc(s_old,s_new,o+1,d)
    elif s_old[o].lower() == s_old[o]:
        return s_new[d].lower()+keep_punc(s_old,s_new,o+1,d+1)
    else: return s_new[d]+keep_punc(s_old,s_new,o+1,d+1)
    
def we_know(k,s):
    s_old = s
    s=[i.upper() for i in s if i.isalpha()]
    k=[i.upper() for i in k if i.isalpha()]

    diff = tuple(ltn(i)+1 for i in k)
    s_new =tuple(ntl((ltn(s[i])-diff[i%len(k)])+1) 
    for i in range(len(s)))

    s_final = keep_punc(s_old,s_new)
    return s_final