def substring_sums(s,k,m):

    sub_strings = []

    for i in range(len(s)):
        for j in range(i + 1, min(i + k + 1, len(s) + 1)):
            sub_strings.append(s[i:j])
    
    sub_strings_ints = [int(x) for x in sub_strings]

    return sum(sub_strings_ints) % m

assert substring_sums('31415', 2, 1000) == 115, substring_sums('31415', 2, 1000)
assert substring_sums('31415', 2, 100) == 15, substring_sums('31415', 2, 100)



