#Prac 2a - First Letters
def first_letters(words):
    return tuple((w[0] for w in words),)
    
#print(first_letters(('can', 'i', 'have', 'this', 'dance')))