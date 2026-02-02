#Prac 2a - First Letters
def first_letters(words):
    return tuple((w[0] for w in words),)
    
#print(first_letters(('can', 'i', 'have', 'this', 'dance')))

#Prac 2b - Triangular Numbers
def triangular_numbers(nums):
    return tuple(((n*(n+1))//2) for n in nums)

#print(triangular_numbers((3, 1, 4, 1)))

#Prac 2c - Doublets
def doublets(words):
    return tuple(w for w in words if w[:((len(w)) // 2)] == w[(len(w)) // 2:])
#print(doublets(('haha', 'lapulapu', 'paruparo', 'litolapidlitolapid')))

#Prac 2d - Odds
def odds_in_range(x, y):
    return frozenset(tuple(n for n in range(x,y+1) if n % 2 != 0))
#print(odds_in_range(3, 7))
#print(odds_in_range(-8, -2))

#Prac 2e - Exactly One
def in_exactly_one(l, s1, s2):
    return tuple(n for n in l if n in s1 ^ s2)

"""print(in_exactly_one(
    (3, 1, 4, 1, 5, 9, 2),
    frozenset((3, 0, 5, 6)),
    frozenset((2, 1, 5)),
))"""

#Pracx 2f - Range-Containing Sets
def sets_containing_range(x, y, intsets):
    important = frozenset(range(x,y+1))
    return tuple(thing for thing in intsets if thing >= important)

"""print(sets_containing_range(3, 6, (
    frozenset((3, 4, 5, 6, 7)),
    frozenset((2, 3, 4, 5, 6, 8)),
    frozenset((1, 2, 3, 5, 6, 7, 8)),
    frozenset(()),
    frozenset((3, 4, 5, 6)),
    frozenset((1, 2, 3, 4, 5)),
    frozenset((4, 5, 6, 7, 8)),
    frozenset((1, 2, 3, 4, 5, 6, 7, 8)),
)))"""

#Prac 2g - Basenames of Text Files
def text_file_bases(filenames):
    return tuple(file[0:len(file)-4] for file in filenames if file[-4:] == ".txt")

"""print(text_file_bases((
    'hello.txt',
    'fromtheoutside.jpg',
    'lol.text',
    'lol.png.txt',
    'lol.png.png',
    'lol.txt.txt',
    'lol',
    'txt.txt.txt',
    'txt.txt.lol',
    'lolo.txt',
)))"""

#Prac 2h - Product of Pairs with Sum
def products(s1, s2, s):
    return frozenset(x*y for x in s1 for y in s2 if x + y == s) #Pair things separately not (x,y) in s1,s2


"""print(products(
    frozenset((3, 1, 4, 2, 5)),
    frozenset((4, 6, 8, 10, 12)),
    9,
))"""

#Prac 2i - Join
def seq_join(seqs):
    return tuple(n for seq in seqs for n in seq) #if looking for n in a set in a set then do a double for from out to in

#print(seq_join(((3, 1, 4), (1, 5), (9, 2, 6))))

#Prac 2j - Join with Delimiter
def seq_join0(seqs):
    each_with_0 = tuple((0,) + seq + (0,) for seq in seqs)
    return tuple(n for seq in each_with_0 for n in seq) 

#print(seq_join0(((3, 1, 4), (1, 5), (9, 2, 6))))

#Prac 2k - Zigzags
def zigzags(seq):
    n = len(seq)
    return frozenset(
        (seq[i], seq[j], seq[k])
        for i in range(n-3)
        for j in range(i+1,n-2)
        for k in range(j+1,n-1)
        if (seq[i] <= seq[j] >= seq[k]) or (seq[i] >= seq[j] <= seq[k])
    )

print(zigzags((3, 1, 4, 1, 5, 9, 2)))

#Lecture problems
def even_sum_pairs(seq1, seq2):
    return tuple((x,y) for x in seq1 for y in seq2)# if (x + y) % 2 == 0)
"""print(even_sum_pairs((2,7,1),(1,2,3)))"""

