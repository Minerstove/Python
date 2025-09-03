#Prac 2a - First Letters
def first_letters(words):
    first_letters = ()
    i=0
    for i in range(len(words)):
        first_letters = first_letters + (words[i][0],)
    return first_letters
    
print(first_letters(('can', 'i', 'have', 'this', 'dance')))