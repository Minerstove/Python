def draw(s, char = ".", hollow = False):
    if hollow == False:
        fill = char
    else:
        fill = " "

    mid = char + f' {fill}' * (s - 1 + s - 2) + " " + char
    cur_s = mid
    lower = []
    for x in range(1, s - 1):
        cur_s = cur_s[:-3] + char
        space = " " * x
        lower.append(space + cur_s + space)
        

    bottom = " " * (s - 1) + f'{char} ' * (s - 1) + char + " " * (s - 1 )

    res = [bottom] + lower[::-1] + [mid] + lower + [bottom]

    assert len(res) == 2 * s - 1
    for string in res:
        assert len(string) == 4 * s - 3

    return res

assert draw(2, char='_', hollow=True) == [
    " _ _ ",
    "_   _",
    " _ _ ",
], draw(2, char='_', hollow=True)

print("\n".join(draw(5,hollow=True)))
print("\n".join(draw(10,hollow=True)))