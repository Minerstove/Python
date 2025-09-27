def draw_fortune_cookie(q):
    def helper(final, start, fortune_cookie_tuple):
        if final == 1:
            return "##\n##\n"
        
        if start == final:
            return "\n" + "".join(new_liner(fortune_cookie_tuple, "\n"))
        
        dots_on_either_side = "." * (2 ** (start - 1))
        fortune_cookie_top_layers = tuple(
            dots_on_either_side + layer + dots_on_either_side 
            for layer in fortune_cookie_tuple)
        fortune_cookie_bottom_rows = tuple(
            row + row for row in fortune_cookie_tuple
        )
        fortune_cookie_tuple = fortune_cookie_top_layers + fortune_cookie_bottom_rows

        return helper(q, start + 1, fortune_cookie_tuple)

    return helper(q, 1, ("##", "##"))

def new_liner(tup, newline):
    if len(tup) == 0:
        return ()
    
    return (tup[0], newline) + new_liner(tup[1:], newline)

#print("".join(new_liner(("HI","HELLO","UWU"), "\n")))

#print(draw_fortune_cookie(1))
print(draw_fortune_cookie(2))
print(draw_fortune_cookie(3))
print(draw_fortune_cookie(4))

"""       
if q == 1:
        return "##\n##\n"
    elif q == 2:
        return ".##.\n.##.\n####\n####\n"
    elif q == 3:
        return "...##...\n...##...\n..####..\n..####..\n.##..##.\n.##..##.\n########\n########\n"""