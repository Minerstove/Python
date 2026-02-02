def show_to_cooking_mama(n, a, b):
    if a == b:
        if n % a == 0:
            return "Wow! Even better than Mama!"
        else:
            return "It's okay. Mama will help you."
    else:
        def helper(cur_a, cur_b):
            product = cur_a * cur_b

            if product == n:
                return True
            if product > n:
                return False

            res_a = helper(cur_a * a, cur_b) if a != 1 else False
            res_b = helper(cur_a, cur_b * b) if b != 1 else False

            return res_a or res_b

        if helper(1, 1):
            return "Wow! Even better than Mama!"
        else:
            return "It's okay. Mama will help you."

assert show_to_cooking_mama(6, 2, 3) == "Wow! Even better than Mama!", show_to_cooking_mama(6, 2, 3)
assert show_to_cooking_mama(5, 2, 3) == "It's okay. Mama will help you.", show_to_cooking_mama(5, 2, 3)

