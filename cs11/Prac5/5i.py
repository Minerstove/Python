def uniquify(seq):
    if not seq:
        return []
    # Handle length 1 naturally by starting with the first element
    uniques = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] != seq[i - 1]:
            uniques.append(seq[i])
    return uniques

            

assert uniquify((
    'hi',
    'hello',
    'hello',
    'hi',
    'hi',
    'hi',
    'hey',
    'hoy',
    'hoy',
    'hi',
    'hello',
    'hello',
)) == [
    'hi',
    'hello',
    'hi',
    'hey',
    'hoy',
    'hi',
    'hello',
], uniquify((
    'hi',
    'hello',
    'hello',
    'hi',
    'hi',
    'hi',
    'hey',
    'hoy',
    'hoy',
    'hi',
    'hello',
    'hello',
))

