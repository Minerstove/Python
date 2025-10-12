def print_all_palindromes(words):
    for str in words:
        if str.lower() == str.lower()[::-1]:
            print(str)

print_all_palindromes((
    'Madam',
    'Webew',
    'Abaca',
    'rawr',
    'lol',
))



