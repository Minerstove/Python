address = list("".join(input().split(".")))
sumaddy = sum(int(x) for x in address)
n = sumaddy % 67 + 1
N = int("".join(address))

def nth_root(N, n):
    if N == 0:
        return 0
    
    if N == 1:
        return 1
    
    lo, hi = 0, N
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        p = mid ** n

        if p == N:
            return mid
        
        if p < N:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans

print(nth_root(N, n))