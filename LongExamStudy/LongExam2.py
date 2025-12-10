##### Number 1
print("two" < "three")

"""
Explanation:
Comparison operators on strings check character by character for order.

so since two and three both start with 't', it goes to 'w' < 'h' which is false since w is after h.
Answer is E.

Key insight:
'a' < 'b' alphabetical
'A' < 'a' Caps come first
'0' < 'A' Digits come first before letters.
"""

##### Number 2
print(*"two")

"""
Answer is E. t w o
Explanation:

Splatting (*) a string splits it into individual characters as separate items.

e.g. [*"cat"] == ['c', 'a', 't']
"""

##### Number 3
print(repr(repr("5"))) # <-- Question
print(repr('5'))
print('5')

"""
Answer is C. "'5'"
Explanation:
repr gives the Python literal representation of the object. So repr('5') == "'5'"
repr("'5'") == ""'5'""

which gets output as "'5'"
"""

##### Number 4
try:
    print('h' - 'a' == 'H' - 'A')
except:
    print("TypeError for - between strings")

"""
Answer is F. an error is raised.
Explanation:
Subtracting strings is not supported natively in python.
"""

##### Number 5
x = 5
y = x
x = 10
print(x + 2 * y)
"""
Answer is based on the idea that immutable variables take on the most recent update.

Meaning that once you equate two immutable variables, x = y, then x will take y's value but not vice versa.

So starting with x, x = 5, then y = x = 5.

Now x = 10 doesn't change y since ints are immutable, so y == 5.

so 10 + 2 * 5 = 20 which is B.

----------------------------

KEY INSIGHT:
Take note that this applies for immutable variables, but once you have a mutable variable (list, etc)

a = [1, 2, 3]
b = a

modifying b will now modify a and vice versa.
"""

##### Number 6
art = (
".|___..|.|",
"...._|_|..",
"_..|.|___.",
"_|_|...._|",
".|___..|.|",
"...._|_|..",
"_..|.|___.",
)
# print(art[x][a:b])
# print(art[y][a:b])
# _|...
# .._|_
"""
Answers. A and B
Explanation:
Quick shortcut is to look at each line of the output
and find parts in the tuple that can match each line.

So for the first print, you can only see it in the fourth row (index 3)
For the second print, you can see it in the 6th and 2nd row. (index 5 and 1)

So x = 3, y = {1, 5}
for art[3][2:7] == "_|..."
for art[1][2:7] == ".._|_"
for art[5][2:7] == ".._|_"

so a = 2, b = 7

Don't forget indexing a list gives from [a, b)
"""

##### Number 7
# (a, (b, c), (d, (e,)), f) = x

"""
Answer is A. (7, (5, 3), (4, (6, (9,), 8)), 1)
Explanation:
I think the easiest path here is elimination. 

B is obviously matching.
C is matching since e can be a tuple
D is matching since b == (5, 4), c == (3,), then so on
E is matching sinec b == (5,), c == 3, e == (6, 9, 8)
F is matching since c == (3,)

A raises an erro because
a == 7, b == 5, c == 3, d == 4,

but the problem is with e which should be a one tuple.
but in (6, (9,), 8), there are 3 elements.

If you would want to fix this A should be
(7, (5, 3), (4, ((6, (9,), 8),)), 1)
so e == (6, (9,), 8)
"""

##### Number 8
# If a and b are tuples, and the assertion
# assert a < b
# passes, then the assertion
# assert frozenset(a) < frozenset(b)
# also passes

"""
Answer is B. sometimes true, sometimes false
Explanation:

for comparison operators on frozensets or sets,
A < B means “A is a proper subset of B”

A <= B means “A is a subset of B”

A > B means “A is a proper superset of B”

A >= B means “A is a superset of B”

for lists/tuples comparison operators look element by element.

So lets look at a counterexample
[5, 3] < [6, 7] -> True since 5 < 6
frozenset({5, 3}) < frozenset({6, 7}) -> False since 5, 3 is not in 6, 7

Lets also see where it is true
[1] < [2, 1] -> True since 1 < 2
frozenset({1}) < frozenset({2, 1}) -> True since 1 is in {2, 1}
"""

##### Number 9
# If a and b are frozensets, and the assertion
# assert a < b
# passes, then the assertion
# assert tuple(a) < tuple(b)
# also passes.

"""
Answer is B. Sometimes true, sometimes false
Explanation:

True Case:
frozenset({1, 2}) < frozenset({1, 2, 3, 4}) -> True
(1, 2) < (1, 2, 3, 4) -> True since (1, 2) is shorter

False Case:
frozenset({5}) < frozenset({1, 5}) -> True
(5,) < (1, 5) -> False since 5 > 1
"""

##### Number 10
def a():
    b()
    c()
def b():
    c()
def c():
    return
    a()

a()
"""
a() is called, which calls b() which calls c(), then c() called in a().

c() does not call a() after the return.

Total 4, which is E.
"""

##### Number 11
print([x**2 for x in {1, 3, 4, 1, 5}])

"""
The answer is E. Undefined.

Explanation:
Sets have no guaranteed order, so the comprehension could read it in any order
theoretically.

could be 
[1, 9, 16, 25]
or
[9, 1, 16, 25]

and it would still be correct.
"""

##### Number 12
print(' '.join(reversed('here i am'.split()))) # <- Question
print(reversed('here i am'.split()))
print('here i am'.split())

"""
Answer: E. am i here
Explanation.
Splitting a string gives a list of each word separated by spaces.
You then reverse that list
then join each element back together into one string.

Giving am i here
"""

##### Number 13
# Suppose the contents of file1.txt are:
# 3
# 10
# and the contents of file2.txt are:
# 10
# 3
# and the contents of code.py are:
# from sys import stderr
# n = int(input())
# print(n**2)
# m = int(input())
# print(n**3, file=stderr)
# If the following bash command is run:
# python3 code.py < file2.txt > file1.txt
# What will be the contents of file1.txt? (There may be multiple possible answers
"""
Answer is D. 100
Explanation:
python3 code.py < file2.txt > file1.txt
    - means that we run code.py with input from file2.txt and output it into file1.txt

so n = 10, m = 3
print(n**2) puts 100 into file1.txt (overwriting everything)
print(n**3) puts 1000 into file=stderr not file1.txt 

So 100 is the only line in file1.txt
"""

##### Number 14
"""
Answer: F. 1000
Explanation:
file=stderr make it so 1000 is output into the terminal stream (stderr is a bit more complicated but eh)
"""

##### Number 15
a = 'wingardium leviosa'
b = 'EXPECTO PATRONUM'
print(any(c in a for c in b))

"""
Answer: D. True
Explanation:
The code is essentially, does any character in b also belong in a?

And there is one! the " "
"""

##### Number 16
symmetry = {
'b': 'd',
'd': 'b',
'p': 'q',
'q': 'p',
'n': 'u',
'u': 'n',
}
start = 'doobidoonunubidapdapnu'
# end = ''.join(...)
"""
Answer: G.
Explanation:
Take a look at the symmetry dictionary. It flips letters.

Now take a look at start vs end. Some letters are in symmetry and others are not.

The letters not in symmetry stay the same.

So were looking if k is in symmetry then we flip it else keep it as it was in start
    - In code: (symmetry[k] if k in symmetry else k for k in start)
"""

##### Number 17
print((lambda f: lambda g: lambda x: f(g(x)))(lambda x: x*3)(lambda x: x+3)(3))
"""
Output is 18
Explanation:
Try reframing the lambdas into this.
print(
    (lambda f:
        lambda g:
            lambda x:
                f(g(x))
    )
    (lambda x: x * 3) # relates to f
    (lambda x: x + 3) # relates to g
    (3)
)
f(x) == lambda x: x * 3
g(x) == lambda x: x + 3

so f(g(x)) == lambda x: (x + 3) * 3

x == 3 so f(g(3)) == 18
"""

##### Number 18
(a, b) = (3, 1)
while b <= 10**3:
    print(a, b)
    (a, b) = (b, a + 2*b)
print(a)

"""
Answer: 915
Explanation:
Let's run a trace.

(3, 1)
(1, 5)
(5, 11)
(11, 27)
(27, 65)
(65, 157)
(157, 379)
(379, 915)
(915, 2204) b > 1000

so a = 915
"""

##### Number 19
def inc_last(vals):
    vals[-1] += vals[-1]
    return vals[-1]

# inc_last((3,1,4))
# inc_last("314")
"""
Answer: B, C, D

Explanation:
If you want to change an element of a sequence, it must be mutable.

Lets see which inputs are immutable.
These are B and C. These give TypeErrors since they do not support item assignment
    - Cuz they are immutable.

Next since dictionaries have keys, the key [-1] must exist,
but D does not have a key of -1 so it will raise a KeyError
"""

##### Number 20
def f(seq):
    return [x * y for (x, y) in seq]
for v in f(((3, 2), ("x", 2), (3, "y"))):
    print(v)

"""
Answer:
6
xx
yyy

Explanation:
for every x, y in seq it will return the product.

3*2=6
"x"*2="xx"
3*"y"="yyy"

boogsh
"""

##### Number 21
"""
Answer is none:

Lets look at option A:
x is not defined -> error

Lets look at option B:
('a' or 'e' or 'i' or 'o' or 'u') in x == 'a' 
    - in python since 'a' is a truthy value (not empty)
    - So it only checks a rather than all vowels

Lets loot at option C:
Similar issue an('aeiou') results in True, and True in "string" returns False
    - Since all chars are truthy if not empty

Lets look at Option D:
This makes us check if the substring 'aeiou' is in the word rather than each character.
    - False

Lets look at Option E;
E should work. but x is not defined.

Actually x is not defined for any option so theyre all wrong!
"""

##### Number 22
from enum import Enum
def make():
    class Color(Enum):
        BLACK = 1
        WHITE = 2
    return Color

Color1 = make()
Color2 = make()

print(Color1.BLACK == Color1.BLACK)

"""
True because an object is equal to itself
"""

##### Number 23
"""
True because an object is itself
"""

##### Number 24
"""
False because they don't refer to the same value Color2 and Color1 are diff objects
because of how Enums work
"""

##### Number 25
"""
False because they don't refer to the same value Color.BLACK != 1 because of how Enums work
"""

##### Number 26
"""
An error is raised because Color is not defined.
"""

##### Number 27
s = 'diner'
pairs = tuple(
    (v, c)
    for v in s
    if v in 'aeiou'
    for c in s
    if c not in 'aeiou'
    )
print(pairs[2])

"""
Lets run a trace!

d: d not in 'aeiou'
i: i in aeiou (i, )
    d: not in aeiou (i, d)
    i: in aeiou
    n: not in aeiou (i, n)
    e: in aeiou
    r: not in aeiou (i, r)

result is ('i', 'r')
"""

##### Number 28
s = 'nature'
triples = tuple(
    (s[l], s[l + (w // 2)], s[l + w - 1])
    for w in range(3, len(s) + 1, 2)
    for l in range(len(s) - w + 1)
    )
print(len(triples))

"""
Answer: 6
Explanation:
len(s) == 6

w = 3 and 5 only

when w = 3
l = 0,1,2,3
4 tuples

when w = 5
l = 0,1
2 tuples

so total of 6 tuples.

Key Insight:
You can ignore some things if only one paramter is being asked for (in this case
no need to index s)
"""