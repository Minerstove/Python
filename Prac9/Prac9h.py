def roman_numeral_value(table, s):
    total = 0
    max_right = 0
    for ch in reversed(s):
        v = table[ch]
        if v < max_right:
            total -= v
        else:
            total += v
            max_right = v
    return total


assert roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VIII') == 8, roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VIII')

assert roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'IV') == 4, roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'IV')

assert roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VID') == 494, roman_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VID')

assert roman_numeral_value({
    'Y': 10,
    'A': 3,
    'P': 5,
}, 'PAPAYA') == -3, roman_numeral_value({
    'Y': 10,
    'A': 3,
    'P': 5,
}, 'PAPAYA')

assert roman_numeral_value({
    'P': 1,
    'L': 1,
    'A': 1,
    'Y': 1,
}, 'PAPAYA') == 6, roman_numeral_value({
    'P': 1,
    'L': 1,
    'A': 1,
    'Y': 1,
}, 'PAPAYA')


