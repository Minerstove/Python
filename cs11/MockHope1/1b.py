def triangle_kind(a,b,c):
    if a + b <= c or b + c <= a or a + c <= b:
        return "degenerate"
    
    if a == b == c:
        return "equilateral"
    
    if a == b or b == c or a == c:
        return "isosceles"
    
    else:
        return "scalene"
    
assert triangle_kind(7, 7, 7) == 'equilateral', triangle_kind(7, 7, 7)
assert triangle_kind(314, 159, 265) == 'scalene', triangle_kind(314, 159, 265)
assert triangle_kind(3, 5, 10) == 'degenerate', triangle_kind(3, 5, 10)

