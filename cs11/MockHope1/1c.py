def evaluate_op(equation):
    operation = equation[0]
    
    x, y = equation[2:len(equation) - 1].split(",")

    if operation == "A":
        return int(x) + int(y)
    elif operation == "S":
        return int(x) - int(y)
    elif operation == "M":
        return int(x) * int(y)

assert evaluate_op("A(5,1)") == 6, evaluate_op("A(5,1)")
assert evaluate_op("S(314,159)") == 155, evaluate_op("S(314,159)")
assert evaluate_op("A(314,-159)") == 155, evaluate_op("A(314,-159)")
assert evaluate_op("M(3,5)") == 15, evaluate_op("M(3,5)")

#DONE

