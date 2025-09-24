#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def we_know(key, s):
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(ch for ch in key if ch.isalpha())  # strip non-letters
    key = key.upper()

    def shift_val(ch):
        return alphabet.index(ch)  # A=0, B=1, ...

    def helper(t, j):
        if not t:
            return ""
        ch = t[0]
        if ch.isalpha():
            k = shift_val(key[j % len(key)])
            # shift backwards for decryption
            p = alphabet[(alphabet.index(ch.upper()) - k) % 26]
            # preserve case
            if ch.islower():
                p = p.lower()
            return p + helper(t[1:], j + 1)
        else:
            return ch + helper(t[1:], j)

    return helper(s, 0)


print(we_know("RIGHT", "OAVVA"))
"""
def _enumerate(s,i):
    if len(s) == 0:
        return ()
    return ((i, s[0]),) + _enumerate(s[1:], i)
"""



#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()