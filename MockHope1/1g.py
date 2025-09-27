def show_to_cooking_mama(n, a, b):

    def is_power_of(num, base):
        if num == 1:
            return True
        if base == 1:
            return num == 1
        if num % base != 0:
            return False
        return is_power_of(num // base, base)
    
    def check_divisibility_by_power(n, a, b, current):
        if current > n:
            return False
        if n % current == 0:
            if is_power_of(n // current , b):
                return True
            
        if a == 1:
            return False
        return check_divisibility_by_power(n,a,b,current*a)
        
    if check_divisibility_by_power(n,a,b,1):
        return "Wow! Even better than Mama!"
    else:
        return "It's okay. Mama will help you."
    
assert show_to_cooking_mama(6, 2, 3) == "Wow! Even better than Mama!", show_to_cooking_mama(6, 2, 3)
assert show_to_cooking_mama(5, 2, 3) == "It's okay. Mama will help you.", show_to_cooking_mama(5, 2, 3)



