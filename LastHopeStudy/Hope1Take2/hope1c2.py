def evaluate(equation):
    equation = equation.replace(" ", "").replace("+", "")

    def helper(equation, minus_counter, current_val):
        if not equation:
            return current_val
        if equation[0] != "-":
            current_val = current_val + value_assign(int(equation[0]), minus_counter)
            return helper(equation[1:], 0, current_val)
        
        return helper(equation[1:], minus_counter + 1, current_val)
    
    def value_assign(val, minus_counter):
        if minus_counter % 2 == 0:
            return val
        else:
            val = -val
            return val
    
    return helper(equation, 0, 0)

assert evaluate("3 + 4") == 7, evaluate("3 + 4")
assert evaluate("3 - -4") == 7, evaluate("3 - -4")
assert evaluate("3-- 4") == 7, evaluate("3-- 4")
assert evaluate("- -- - --- - 3- - - - -- - 4") == -1, evaluate("- -- - --- - 3- - - - -- - 4")
assert evaluate("- +- - --+ + 3+ + - - ++ - 4") == -7, evaluate("- +- - --+ + 3+ + - - ++ - 4")
assert evaluate("--1   +2   -3") == 0, evaluate("--1   +2   -3")
