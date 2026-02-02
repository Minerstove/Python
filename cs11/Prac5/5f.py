def partial_sums(seq):
    partial_sum_seq = [0]

    for i in range(len(seq)):
        next_sum = partial_sum_seq[i] + seq[i]
        partial_sum_seq.append(next_sum)
        print(partial_sum_seq)

    return sorted(partial_sum_seq)

assert partial_sums((3, 1, 4, 1)) == [0, 3, 4, 8, 9], partial_sums((3, 1, 4, 1))
assert partial_sums((1,)) == [0, 1], partial_sums((1,))
