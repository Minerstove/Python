def identify_cell(center, p, k):
    ci, cj = center

    if k < 1 or k > num_p(p):
        return None

    def helper(ci, cj, p, k):
        if p == 0:
            return (ci, cj)

        d = 1 << (p - 1)  # 2**(p-1)

        size_small = num_p(p - 1)

        diag_len = 2 * d + 1  # = 2**p + 1

        if k <= size_small:
            return helper(ci - d, cj - d, p - 1, k)

        k = k - size_small

        if k <= diag_len:
            t = k - 1
            i = ci - d + t
            j = cj - d + t
            return (i, j)

        k = k - diag_len

        return helper(ci + d, cj + d, p - 1, k)

    return helper(ci, cj, p, k)

def num_p(p):
    if p == 0:
        return 1
    return 2 * num_p(p - 1) + (1 << p) + 1