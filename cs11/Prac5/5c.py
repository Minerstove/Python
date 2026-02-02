def fibs(n):

    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    fib_sequence = [0, 1]

    for i in range(n - 2):
        first, second = fib_sequence[i], fib_sequence[i + 1]
        next_num = first + second

        fib_sequence.append(next_num)
    
    return fib_sequence

assert fibs(8) == [0, 1, 1, 2, 3, 5, 8, 13], fibs(8)

"""
def fibs(n):
    if n <= 0:
        return []
    
    fib_sequence = [0] * n   # preallocate space
    fib_sequence[0] = 0
    
    if n > 1:
        fib_sequence[1] = 1
        for i in range(2, n):
            fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    
    return fib_sequence

more efficient version by a bit. More readable because it makes use of the mutability of lists by assigning specific parts of a list to a value
"""



