def seq_join(seqs):

    splatted_seq = [] * len(seqs)

    for seq in seqs:
        splatted_seq.extend([*seq])

    return splatted_seq

assert seq_join(((3, 1, 4), (1, 5), (9, 2, 6))) == [3, 1, 4, 1, 5, 9, 2, 6], seq_join(((3, 1, 4), (1, 5), (9, 2, 6)))
