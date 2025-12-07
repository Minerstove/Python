# # Pinoy Party
# from functools import cache

MOD = 1_000_000_007
MAXN = 1_000_005

dp = [0] * (MAXN + 1)
dp[0] = 1
dp[1] = 2
dp[2] = 4
dp[3] = 9

for i in range(4, MAXN + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD


def num_sticks(n):
    if n <= 3:
        return 0

    all_hotdogs = 1 if n % 3 == 0 else 0
    all_marshmallows = pow(2, n, MOD)

    return (dp[n] - all_hotdogs - all_marshmallows) % MOD
# def num_sticks(n):
#     if n <= 3:
#         return 0
    
#     modulo = 1000000007    

#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[1] = 2
#     dp[2] = 4
#     dp[3] = 9

#     for i in range(4, n + 1):
#         dp[i] = (2 * dp[i - 1] + dp[i - 3]) % modulo

#     all_hotdogs = 1 if n % 3 == 0 else 0    
#     all_marshmallows = pow(2, n, modulo)

#     return (dp[n] - all_hotdogs - all_marshmallows) % modulo
    # @cache
    # def _num_sticks(n):
    #     if n == 0:
    #         return 1
    #     elif n == 1:
    #         return 2
    #     elif n == 2:
    #         return 4
    #     elif n == 3:
    #         return 9
        
    #     return 2 * _num_sticks(n - 1) + _num_sticks(n - 3)
    
    # total_no_constraints = _num_sticks(n)
    
    # all_hotdogs = 1 if n % 3 == 0 else 0    
    # modulo = 1000000007
    # all_marshmallows = pow(2, n, modulo)

    # return (total_no_constraints - all_hotdogs - all_marshmallows) % modulo


    


# @cache
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n)

# @cache
# def permutations(n, r):
#     return factorial(n)//factorial(n-r)

assert num_sticks(5) == 12, num_sticks(5)
assert num_sticks(6) == 32, num_sticks(6)
from functools import cache

def num_sticks(n):
    ...

@cache
def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n - 1)