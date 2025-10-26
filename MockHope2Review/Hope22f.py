def tail_and_cycle(f,s):
    current = s
    appeared = {s}
    processed = [s]
    previous_occ = {s: 0}
    index = 0

    while True:
        current = f[current]
        index += 1

        if current in appeared:
            return(
                processed[:previous_occ[current]],
                processed[previous_occ[current] : index],
            )

        appeared.add(current)
        previous_occ[current] = index
        processed.append(current)
    
assert tail_and_cycle((2, 3, 1, 0), 1) == ([], [1, 3, 0, 2]), tail_and_cycle((2, 3, 1, 0), 1)
assert tail_and_cycle((2, 2, 1, 5, 0, 3), 0) == ([0], [2, 1]),tail_and_cycle((2, 2, 1, 5, 0, 3), 0)


