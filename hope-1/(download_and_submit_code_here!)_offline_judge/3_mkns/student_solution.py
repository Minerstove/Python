#put your solution here
#i can't check constraints, so just be honest hehe

#---to test your code, RUN this file---
def mkns(n,k):
    radius = n**k
    base = radius**2
    
    def get_next_layer(base, radius, height):
        if base <= 0:
            return 0
        new_layer = base - (2*height*radius + radius**2)
        return new_layer + get_next_layer(new_layer, radius - 1, height + 1)
    
    return base + get_next_layer(base, radius, 1)

"""
    def get_cylinder_ounces(radius,h):
        ounces = h*(radius**2)
        return ounces
    
    def recursive_helper(radius, h):
        if radius == 0:
            return 0
        return get_cylinder_ounces(radius, h) + recursive_helper(radius - 1, h + 1)
    
    return recursive_helper(radius, 1) % 23412143"""

#---to test your code, RUN this file---

if __name__ == "__main__":
    from tester import run_tests
    run_tests()