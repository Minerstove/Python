def mkns(n, k):
    MOD = 23412143
    a = pow(n, k, MOD)
    inv12 = pow(12, -1, MOD)

    a2 = (a*a) % MOD
    a3 = (a2*a) % MOD

    poly = (a3+4*a2+5*a+2) % MOD
    num = (a*poly) % MOD

    return (num*inv12) % MOD
