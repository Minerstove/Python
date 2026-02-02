def ramon_numeral_value(r, n):
    s = 0
    for c in n: s += r[c]
    return s

assert ramon_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VIII') == 8, ramon_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'VIII')

assert ramon_numeral_value({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}, 'IV') == 6

assert ramon_numeral_value({
    'Y': 10,
    'A': 3,
    'P': 5,
}, 'PAPAYA') == 29, ramon_numeral_value({
    'Y': 10,
    'A': 3,
    'P': 5,
}, 'PAPAYA')


