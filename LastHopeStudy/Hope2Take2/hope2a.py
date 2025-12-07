def earnings(slices, groups):
    result = []
    for group in groups:
        tokens = 0
        for cake in slices:
            if cake % group == 0:
                tokens += cake
        
        result.append(tokens)

    return result

assert earnings([2, 10, 15], [1, 3, 5]) == [27, 15, 25], earnings([2, 10, 15], [1, 3, 5])
