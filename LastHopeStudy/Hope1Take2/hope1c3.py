def count_occ(s, i, j, c):
    def helper(idx, depth, pos):
        if idx == len(s) or pos >= j:
            return 0, pos

        ch = s[idx]

        if ch == '[':
            return helper(idx + 1, depth + 1, pos)

        if ch == ']':
            return helper(idx + 1, depth - 1, pos)

        mult = 1 << depth
        start = pos
        end = pos + mult

        add = 0
        if ch == c:
            if end > i and start < j:
                overlap_start = max(start, i)
                overlap_end = min(end, j)
                add = overlap_end - overlap_start

        rest, final_pos = helper(idx + 1, depth, end)
        return add + rest, final_pos

    total, _ = helper(0, 0, 0)
    return total


assert count_occ("a[ba[na]]q[ue]", 1, 9, "a") == 4, count_occ("a[ba[na]]q[ue]", 1, 9, "a")
assert count_occ("ni[[ha]]", 0, 4, "k") == 0, count_occ("ni[[ha]]", 0, 4, "k")

