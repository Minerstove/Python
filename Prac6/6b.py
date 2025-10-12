def bad_section_count(heights):
    n = len(heights)
    bad_sections = 0

    for i in range(n):
        prev, curr, nxt = heights[i - 1], heights[i], heights[(i + 1) % n]
        if (curr < prev and curr < nxt) or (curr > prev and curr > nxt):
            bad_sections += 1

    return bad_sections



assert bad_section_count((3, 1, 4, 1, 5, 9, 2, 6, 5)) == 6, bad_section_count((3, 1, 4, 1, 5, 9, 2, 6, 5))
assert bad_section_count((5, 5, 5)) == 0, bad_section_count((5, 5, 5))
assert bad_section_count((1, 2, 2, 2)) == 1, bad_section_count((1, 2, 2, 2))