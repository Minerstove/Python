#SAMPLEX 1
#### Number 1
try:
    print(print("2" < 3))
except:
    print("Question 1 gives a TypeError because strings and ints cannot be compared")

##### Number 2
"""
if not (a % 5 != 0) and a % 7 == 0:
if you look at it in terms of propositional logic where
P represents the statement a % 5 != 0 and
Q represents the statement a % 7 == 0
you have ~P ^ Q

You can try truth tables or just apply some rules:
Here are solutions for the answers.

F. if not (a % 5 != 0 or not (a % 7 == 0)) <-> ~(P v ~Q)
~P ^ Q      Premise
~(P v ~Q)   Demorgan's Law

C. if not (a % 5 != 0 or a % 7 != 0): <-> ~(P v ~Q) 
Same solution as above but notice statement Q is negated (== vs !=)
"""

##### Number 3
with open("file.txt", "r") as f:
    """
    Contents originally:
    3
    14
    """
    n = int(f.readline())
with open("file.txt", "w") as f:
    """
    Contents now:
    9
    """
    f.write(str(n * n))

"""
Explanation:
when we have open a file as r, then we open it to read. 
So this function reads the first line only which is 3, making n = 3

then it closes the file.

now it opens the file as w or write, which *overwrites* the original
content with n * n which is 9

answer: 9
"""

##### Number 4
ans = 0
# Remember that ranges are zero indexed (Key Insight)
for i in range(2): #First loop gives zero, meaning that j loop is only triggered once.
    for j in range(2 * i): # Second loop of i gives 1, so same thing with previous, only k is triggered once.
        for k in range(2 * j): # Same
            for l in range(2 * k): # Same
                for m in range(2 * l): # Same, so when k = 1, it loops twice, so ans results in 2
                    ans += 1
print(ans)
# Answer is G btw.

##### Number 5
x = 2
y = x
x = 5
x = y
print(x + 100 * y)
"""
Answer is based on the idea that immutable variables take on the most recent update.

Meaning that once you equate two immutable variables, x = y, then x will take y's value but not vice versa.

So starting with x, x = 2, then y = x = 2.

Now x = 5 doesn't change y since ints are immutable, so y == 2.

x = y = 2 -> x = 2

so 2 + 100 * 2 = 202 which is D.

----------------------------

KEY INSIGHT:
Take note that this applies for immutable variables, but once you have a mutable variable (list, etc)

a = [1, 2, 3]
b = a

modifying b will now modify a and vice versa.
"""

##### Number 6
def f(x, y):
    return [x] * y
def g(x, y):
    return [y] * 2 * x
res = []
for i in range(1, 3 + 1):
    for j in range(1, 5 + 1):
        res += f(i, j) + g(i, j)
print(len(res))

"""
Explanation:

You make use of the idea that i and j are variables, so
f(i, j) == [i] * j elements
g(i, j) == [i] * 2 * j elements

essentially you can ignore i and just focus on j and multiply it to how many i loops there are
    - Since i is just an element and you are looking for len(res)

1, 2, 3 (3 loops)
1, 2, 3, 4, 5 (5 j values)

f(i, j) + g(i, j)   == [i] * j + [i] * 2 * j
                    == [i] * (j + 2 * j)
                    == [i] * (3 * j)
by some extrapolation each loop is worth 3j elements

so 3 + 6 + 9 + 12 + 15 = 45
45 * 3 = 105

Answer is C.
"""

##### Number 7
    #012345678901234567890
s = 'GCCTTAAGGGGGCCTGCGTTTTCTGCCTGTCGATC'

# which of the following results to ['C', 'A', 'G', 'G', 'T']?
"""
Explanation:
Your first idea might be to trial and error everything, but theres a quick filter method you can try

Notice that C is the first element of the list and G is the first char of the string.

Therefore you can eliminate A, B, C immediately.

Next Remember that indexing is in the form of s[a:b] -> you get elements from [a, b) (b is exclusive so check until b - 1)

So lets look at the end indexes of D, E, F. 
s[13] == C, s[14] == T, s[15] == G

Notice the last element of the list is T? so our candidate is currently E.
Lets Verify, there is a step of 3 in E so

s[2] == C
s[5] == A
s[8] == G
s[11] == G
s[14] == T

Therefore the answer is E.
"""

##### Number 8
art = (
    '---+---+---+---+---+',
    '.o.|.o...o.|.o...o.|',
    '---+---+---+---+---+',
    '.o...o.|.o...o.|.o..',
    '---+---+---+---+---+',
    '.o.|.o...o.|.o...o.|',
    '---+---+---+---+---+',
)

"""
Explanation:
first we reverse the list giving us this 
- (better if you noticed it was symmetrical from the start 
   so you could've skipped this step)

(
    '---+---+---+---+---+', 
    '.o.|.o...o.|.o...o.|', 
    '---+---+---+---+---+', 
    '.o...o.|.o...o.|.o..', 
    '---+---+---+---+---+', 
    '.o.|.o...o.|.o...o.|', 
    '---+---+---+---+---+'
)

Access the art[3] (fourth row)

art[3] == '.o...o.|.o...o.|.o..'

now access the art[3][7] (8th char)

art[3][7] == | so answer is B.
"""

##### Number  9 

a = 1
b = 2
c = 3
for _ in range(5):
    [b, c, a] = [a, b, c]
for _ in range(5):
    [c, a, b] = [a, b, c]

print(a, b, c)

"""
Explanation:

notice that a cycle of 3 repeats every 3 steps, # Key Insight: This is generalizable
so a loop running 5 times is the same as the loop run twice
    - 5 % 3 == 2

quickly running the first loop twice.
Loop 1
b = 1
c = 2
a = 3

Loop 2
b = 3
c = 1
a = 2

now run the second loop twice
c = 2
a = 3
b = 1

Loop 2
c = 3
b = 2
a = 1

now print(a, b, c) gives 1 2 3 which is A.
"""

##### Number 10
print({3, 1, 4, 1, 5} == {3, 1, 4, 5})

"""
A set checks if all unique elements in itself are in the other set. Since 1, 3, 4, 5 are in both sets
then it evaluates to True which is C.
"""

##### Number 11
print({3, 1, 4, 1, 5} is {3, 1, 4, 5})
"""
Unlike number 10, the is comparison operator checks if they are the same *object*
meaning that if you have for example a and b, a == b can be true, but a can never be b because 
they are diff objects.

Key Insight:
Variables are stored as some kind of thing in the computer and is checks if the thing is the thing.

so you can also do 
print({3, 1, 4, 5} is {3, 1, 4, 5}) == False

Since they go to diff things in the computer. Lowkey wait for upper CS for more explanations
"""

##### Number 12
R = C = 11
g = [[(i + j) % 3 for j in range(C)] for i in range(R)]
s = set()
for i in range(R - 1):
    for j in range(C - 1):
        gg = tuple(
            tuple(g[ii][jj] for jj in range(j, j + 2))
            for ii in range(i, i + 2)
            )
        s.add(gg)
print(len(s))

"""
Explanation:
We can immediately recognize this as a grid problem because the code defines
R and C, then constructs g, a 2D list (a grid) of integers.

The grid g is created using:
    g[i][j] = (i + j) % 3

So the values repeat every 3 steps. For example, some rows look like:

[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
[1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
[2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

You can see the pattern shifts by +1 each row, but still repeats mod 3.

Now look at the nested loops:

for i in range(R - 1):
    for j in range(C - 1):

These loops slide over every possible 2x2 subgrid of g.  
For each position (i, j), the code extracts the 2x2 block:

    [[g[i][j],     g[i][j+1]],
     [g[i+1][j],   g[i+1][j+1]]]

This block is then converted to a tuple-of-tuples and inserted into a set s.
Since sets automatically remove duplicates, the problem effectively asks:

    “How many *distinct* 2x2 subgrids appear in g?”

Finally, it prints len(s).

A 2×2 subgrid has this form:

[i+j,   i+j+1]
[i+j+1, i+j+2]   all mod 3


So if we let k = (i + j) % 3, the block always becomes:

Case 1: k = 0

[0, 1]
[1, 2]


Case 2: k = 1

[1, 2]
[2, 0]


Case 3: k = 2

[2, 0]
[0, 1]


These are the only three possible 2×2 blocks the grid can generate, because:

Every entry is (i+j) mod 3.

Sliding one step diagonally always increases (i+j) by 1 mod 3.

There are only 3 possible values mod 3.

Therefore, the set s ends up containing exactly 3 distinct patterns.

So the printed answer is:

3 which is E.

Lowkey skip this problem LOL but

KEY INSIGHT:
Set usually means how many unique things are in a thing.
Modulo usually means that things repeat.
"""

##### Number 13
def restaurant():
    i_want_dessert = True
    while True:
        yield "appetizer"
        yield "main course"
        if i_want_dessert:
            yield "dessert"
        i_want_dessert = not i_want_dessert

dcdonalds = restaurant() 
for _ in range(10):
    print(next(dcdonalds))

"""
Here we can just run it from 0 - 9
0: "appetizer"
1: "main course"
2: "dessert"
i_want_dessert = False
3: "appetizer"
4: "main course"
i_want_dessert = True
5: "appetizer"
6: "main course"
7: "dessert"
i_want_dessert = False
8: "appetizer"
9: "main course"

Answer is C. 2
"""

#### Number 14
n = 120
se = set()
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) - 1
    print('hello')
    se.add(n % 10)
    if len(se) == 10:
        break

"""
Explanation:
This problem is essentially saying how many times does the while loop trigger.
Lets do a trace!
Loop num: n
0: n = 60: se = {0}
1: n = 30: se = {0}
2: n = 15: se = {0, 5}
3: n = 44: se = {0, 5, 4}
4: n = 22: se = {0, 5, 4, 2}
5: n = 11: se = {0, 5, 4, 2, 1}
6: n = 32: se = {0, 5, 4, 2, 1}
7: n = 16: se = {0, 5, 4, 2, 1, 6}
8: n = 8: se = {0, 5, 4, 2, 1, 6, 8}
9: n = 4: se = {0, 5, 4, 2, 1, 6, 8}
10: n = 2: se = {0, 5, 4, 2, 1, 6, 8}
11: n = 1: se = {0, 5, 4, 2, 1, 6, 8}

And we break the loop since n == 1!

So "hello" is printed 12 times.
"""

##### Number 15
from random import Random
rand = Random(11)
for i in range(10):
    print(rand.randint(0, 1), end=" ")
print()

for i in range(5):
    print(rand.randint(0, 1), end=" ")
print()
"""
Explanation:
rand = Random(11) generates a seed essentially. so rand remains the same.

so it will print the first 5 digits of the rand.

Check zeal documentation for this proof.

answer is B.
"""

##### Number 16
def gen(n: int) -> list[str]:
    if n == 2:
        return ["()"]
    else:
        ans = [f"({inner})" for inner in gen(n - 2)]
        # print(ans)
        for left in range(2, n, 2):
            l = gen(left)
            r = gen(n - left)
            ans += [_l + _r for _l in l for _r in r]
    return ans

print(gen(4))

"""
Explanation:
Take note of the recursive nature of this function.
ans is a list that returns a string based on each element in gen(2).
so ans = ["(())"]

for left in range(2, 4, 2) only loops once since ranges are [a, b)
l = gen(2) = ["()"]
r = gen(2) = ["()"]

we just add l + r since its one element anyway

resulting in ['(())', '()()'] which is B.
"""

##### Number 17
can, we, do, better = "can we do better".split()
[we, can, do, better] = sorted(
(can, we, do, better), key=lambda word: (len(word), word)
)
print(" ".join((can, we, do, better)))

"""
Explanation:
"can we do better".split() == "can", "we", "do", "better"
can == "can"
we == "we"
do == "do"
better == "better"

let us look at the sorted(bla bla)
    - the key makes us sort the things by the length of the word, then by alphabetical order if its a tie.

so sorting (can, we, do, better) gives

("do", "we", "can", "better")

so now
we = "do"
can = "we"
do = "can"
better = "better"

so printing the joined list give sus

we do can better, which is D.
"""
######################################
# FREE FORM QUESTIONS

##### Number 18
def validity(v):
    if v % 5 == 0:
        return 'Yes'
    elif v % 3 == 0:
        return 'Yes'
    else:
        return 'No'

def div_sum(n):
    return sum(
    v
    for v in range(1, n + 1)
    if validity(v) == 'Yes' and validity(v) != 'No'
    )

"""
The main problem with div_sum is that it calls validity(v) twice for every v, 
even though validity always returns either the string "Yes" or "No". 
The condition validity(v) == "Yes" and validity(v) != "No" is therefore redundant: 
whenever validity(v) == "Yes" is true, validity(v) != "No" is automatically true, 
so the second check never removes any values and just repeats the same work. 
This makes the code less efficient and harder to read. 

A cleaner design is to have validity return a Boolean 
and use it once in the comprehension, for example:

def validity(v):
    return v % 5 == 0 or v % 3 == 0

def div_sum(n):
    return sum(v for v in range(1, n + 1) if validity(v))
"""

##### Number 19
def divisible_by_at_least_one(x, y, u, v):
    for num in range(x, y+1):
        if num % u == 0 and num % v == 0:
            yield num
        elif num % u == 0 and num % v != 0:
            yield num
        elif num % u != 0 and num % v == 0:
            yield num

"""
The main problem with the code is that it makes use of several and statements
when the statement attempts to find if something is divisible by at least one of u or v.

This means that it should align more with KISS if you simply use an or statement

so I would fix it by refactoring the code such that.
def divisible_by_at_least_one(x, y, u, v):
    for num in range(x, y+1):
        if num % u == 0 or num % v == 0:
            yield num
"""

##### Number 20
def foo(a, b):
    if a > b:
        raise ValueError("a must not be greater than b")
    return sum(x**2 for x in range(a, b+1) if str(x).startswith('1'))

try:
    res = foo(x, y)
except Exception:
    print('bad')
else:
    print('good', res)

"""
a.
foo(a, b) first checks that a is not greater than b (otherwise it raises a ValueError).
If the order is okay, it goes through all integers from a to b inclusive and selects only those whose decimal representation starts with the digit '1', 
squares each of those numbers, and returns the sum of those squares.
b.
'good' 30922
c.
'bad' # raises a ValueError (look at the code haha)
"""

##### Number 21
"""
for _ in range(n):
    seq.append(f())

vs

seq += [f() for _ in range(n)]

~~

Explanation:
These are different because of how f() is evaluated in the for loop vs the comprehension.

In the for-loop version, each call to f() happens one at a time while seq is actively growing. 
If f() refers to seq (even without mutating it), then each successive call sees a slightly larger seq. 
So the n values produced by f() can depend on the intermediate states of seq.

In the list comprehension version, Python evaluates the entire comprehension in an isolated temporary list before modifying seq at all. 
All n calls to f() happen when seq is still in its original state. Only after the list is fully created does seq += […] extend seq.

Thus, the two expressions can produce different results because f() sees changing seq in the loop version but sees the original seq in the comprehension version.
"""

##### Number 22
def f(xs):
    squares = (x**2 for x in xs)
    for sq in squares:
        if sq % 10 == 9:
            return sq
        
"""
a.
The current code does not enumerate all the squares with last digit 9 in xs, 
but rather it returns the first square in squares that has a last digit of 9.

b.
To address the bug I would rewrite the code as following.
def f(xs):
    squares = (x**2 for x in xs)
    result = [] 
    for sq in squares:
        if sq % 10 == 9:
            result.append(sq)
    return result
"""

##### Number 23
def f(s):
    n = len(s)
    ans, cur = 0, 1
    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            ans = max(ans, cur)
            cur = 1
        else:
            cur += 1
    return ans
assert f('10111001101') == 3

"""
Explanation:
Let's notice that once you reach the last character, you never update ans.

So if you have something like ('111') you would get 2 rather than 3.

So to fix the code you have to add another ans = max(ans, cur) before returning ans after the loop.
"""

##### Number 24
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def mag2(pt):
    return pt.x**2 + pt.y**2

pts = [
    Point(1, -1),
    Point(6, 0),
    Point(0, 9),
    Point(0, 0),
    Point(-2, -2),
    Point(-6, -1),
    Point(-2, 3),
    Point(3, 3),
    ]

for pt in sorted(pts, key=mag2):
    print(f"[at {pt.y}] {pt.x}")

"""
Explanation:

Lets notice that key=mag2 means that we sort the points by the sum of the squares of their respective x and ys.

pts = [
    Point(1, -1), mag2 = 2
    Point(6, 0), mag2 = 36
    Point(0, 9), mag2 = 81
    Point(0, 0), mag2 = 0
    Point(-2, -2), mag2 = 8
    Point(-6, -1), mag2 = 37
    Point(-2, 3), mag2 = 13
    Point(3, 3), mag2 = 18
    ]

sorted pts = [
    Point(0, 0),
    Point(1, -1),
    Point(-2, -2),
    Point(-2, 3),
    Point(3, 3),
    Point(6, 0),
    Point(-6, -1),
    Point(0, 9),
    ]

so the output would be
[at 0] 0
[at -1] 1
[at -2] -2
[at 3] -2
[at 3] 3
[at 0] 6
[at -1] -6
[at 9] 0
"""

##### Number 25
def foo(n):
    if n < 1:
        raise ValueError(f"n must be positive; got {n}")
    def f(a, b):
        d = a**3 - b**3
        if d > n:
            return f(a, b + 1)
        elif d < n:
            return f(a + 1, b)
        else:
            return (a, b)
    
    return f(0, 0)

foo(721)
"""
a.
(9, 2)
b.
f(0,0)
f(1,0)
f(2,0)
f(3,0)
f(4,0)
f(5,0)
f(6,0)
f(7,0)
f(8,0)
f(9,0)
f(9,1)
f(9,2)
c.
def f(a, b):
    d = a**3 - b ** 3
    while d != n:
        if d > n:
            b += 1
        elif d < n:
            a += 1
        d = a**3 - b ** 3 # in f, d is computed before checking the NEXT round.
    return (a, b)
d.
First, suppose foo(n) halts. Then the recursion of f eventually reaches some pair

(a,b)

for which the else branch is taken. That branch is executed only when

a**3 - b**3 == n

Therefore, if foo(n) halts, there exist integers a,b

n == a**3 - b**3; 

i.e., n is a difference of two cubes.

Second suppose n = A**3 - B**3, since f increments a and b by one for every loop depending on the value of d, then eventually it will reach some point A, B.
It cannot pass A, B because increasing a brings d closer to n, so does increasing b.
    - because increasing a when  d<n moves d upward toward n, and increasing b when d>n moves d downward toward n.
Only one variable is incremented by one at a time so it must eventually reach A, B.

Therefore foo(n) halts

Therefore foo(n) halts iff n is a difference of two cubes.
"""