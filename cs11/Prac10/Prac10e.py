from oj import longest_palindrome_substr

def longest_palindrome_after_flip(string):
    n = len(string)
    best = 0

    for i in range(n):
        flipped = '1' if string[i] == '0' else '0'
        t = string[:i] + flipped + string[:i + 1]
        cand = longest_palindrome_substr(t)
        if cand > best:
            best = cand

    return best