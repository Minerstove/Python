def notnot(s):
    s = s.lower()
    S = s.split()

    def word_ctr(s, i=0):
        if not s or s[0] != 'not':
            return i
        else:
            return word_ctr(s[1:], i+1)

    fS = tuple(frozenset(S))
    if len(fS) == 1 and fS[0] == 'not':
        return ((len(S)-1) % 2 == 1) * "not " + "not"

    cnt = word_ctr(S)
    return "not " * (cnt % 2 == 1) + " ".join(S[cnt:])
