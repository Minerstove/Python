def hacker(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):
                sieve[j] = False

    if sieve[n]:
        return (n,)

    for p in range(2,n//2+1):
        if sieve[p] and sieve[n-p]:
            return (p, n-p)