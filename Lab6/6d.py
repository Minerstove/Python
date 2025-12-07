def longest_string_seq(strings):
    if not strings:
        return 0
    
    strings = list(set(strings))
    strings = sorted(strings, key=len)
    n = len(strings)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if strings[j] in strings[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

assert longest_string_seq(('a', 'banana', 'anna', 'ann', 'an', 'hannah', 'an')) == 5, longest_string_seq(('a', 'banana', 'anna', 'ann', 'an', 'hannah', 'an'))
