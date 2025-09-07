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

#Prac 2d - 


def even_sum_pairs(seq1, seq2):
    return tuple((x,y) for x in seq1 for y in seq2)# if (x + y) % 2 == 0)
"""print(even_sum_pairs((2,7,1),(1,2,3)))"""