from prac11h import print_return
from functools import cache

@print_return
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

print(f"result: {fib(5) = }")


@cache
@print_return
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

print(f"result: {fib(5) = }")
assert fib(4) == 3
assert fib(5) == 5

def path_count(grid):
    grid = [*map(''.join, grid)]

    print(*grid, sep='\n')

    assert grid, "grid must be nonempty"

    r, c = len(grid), len(grid[0])

    assert r >= 1 and c >= 1, "grid must be nonempty"
    assert {*map(len, grid)} == {c}, "grid rows must have the same length"

    def in_bounds(i: int, j: int) -> bool:
        return 0 <= i < r and 0 <= j < c

    def get(i: int, j: int) -> str:
        return grid[i][j] if in_bounds(i, j) else '#'

    @cache
    @print_return
    def p(i: int, j: int) -> int:
        if get(i, j) == '#':
            return 0
        elif (i, j) == (r-1, c-1):
            return 1
        else:
            return p(i + 1, j) + p(i, j + 1)

    return p(0, 0)


res = path_count((
    '.....',
    '..#..',
    '.....',
))
print(res)
assert res == 6

def merge(a, b):
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if i < len(a) and (not (j < len(b)) or a[i] <= b[j]):
            yield a[i]; i += 1
        else:
            yield b[j]; j += 1

@print_return
def merge_sort(seq):
    if len(seq) <= 1:
        return tuple(seq)
    else:
        h = len(seq) // 2
        return tuple(merge(merge_sort(seq[:h]), merge_sort(seq[h:])))

res = merge_sort((3, 1, 4, 1, 5, 9, 2, 6))
assert res == (1, 1, 2, 3, 4, 5, 6, 9)

def is_subseq(big, sml):
    if not sml:
        return True
    elif not big:
        return False
    elif big[0] == sml[0]:
        return is_subseq(big[1:], sml[1:])
    else:
        return is_subseq(big[1:], sml)

print(is_subseq('banana', 'anna'))
print(is_subseq('banana', 'anne'))

@print_return
def alph(n, s):
    return '' if n == 0 else chr(ord('a') + s) + alph(n - 1, s + 1)

res = alph(5, 0)
assert res == 'abcde'