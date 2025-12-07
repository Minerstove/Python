def evaluate_op(equation):
    op = equation[0]
    nums = tuple(equation.split(","))
    num1 = int(nums[0][2:])
    num2 = int(nums[1].rstrip(")"))

    if op == "M":
        return num1*num2
    elif op == "S":
        return num1 - num2
    else:
        return num1 + num2
    
assert evaluate_op("A(5,1)") == 6, evaluate_op("A(5,1)")
assert evaluate_op("S(314,159)") == 155, evaluate_op("S(314,159)")
assert evaluate_op("A(314,-159)") == 155, evaluate_op("A(314,-159)")