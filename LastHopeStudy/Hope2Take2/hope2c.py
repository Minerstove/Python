def card_triplets(cards):
    cards = iter(cards)

    try:
        c1 = next(cards)
        c2 = next(cards)
    except StopIteration:
        return

    for c3 in cards:
        f1, s1 = c1[:-1], c1[-1]
        f2, s2 = c2[:-1], c2[-1]
        f3, s3 = c3[:-1], c3[-1]

        if s1 == s3 and f2 != f1 and f2 != f3:
            yield (c1, c2, c3)

        c1, c2 = c2, c3