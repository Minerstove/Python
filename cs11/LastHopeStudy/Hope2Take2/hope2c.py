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

assert [*card_triplets(("2H", "3D", "4H", "5H", "4H"))] == [("2H", "3D", "4H"), ("4H", "5H", "4H")], [*card_triplets(("2H", "3D", "4H", "5H", "4H"))]
assert [*card_triplets(["AC", "2S", "3H", "4D", "5C", "6S", "7H", "8D", "9C", "JS", "QH", "KD"])] == [], [*card_triplets(["AC", "2S", "3H", "4D", "5C", "6S", "7H", "8D", "9C", "JS", "QH", "KD"])]
