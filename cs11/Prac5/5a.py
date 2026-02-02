def last_letters(words):
    letters = []

    for word in words:
        letters.append(word[-1])

    return "".join(letters)

assert last_letters(('can', 'i', 'have', 'this', 'dance')) == 'niese', last_letters(('can', 'i', 'have', 'this', 'dance'))
