from Prac11e import rolling_queue

def verify(condition: bool, message: str = "verification failed"):
    assert condition, message

op1 = rolling_queue([3, 1, 6])
op2 = rolling_queue([3, 1])

verify(op1(2) == 1)
verify(op2(4) == 1)
verify(op2(1) == 1)
verify(op1(2) == 1)
verify(op2(5) == 1)
verify(op1(7) == 2)
verify(op1(7) == 2)
verify(op2(9) == 1)
verify(op2(2) == 2)
verify(op1(6) == 2)
verify(op1(6) == 6)
verify(op2(6) == 2)
verify(op1(0) == 0)
verify(op2(5) == 2)
verify(op2(3) == 3)
verify(op1(1) == 0)
verify(op2(5) == 3)
