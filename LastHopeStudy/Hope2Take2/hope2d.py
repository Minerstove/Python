def translate(ds, i, word, j):
    n = len(ds)

    steps = (j - i) % n

    for _ in range(steps):
        d = ds[i]
        if word not in d:
            return None
        word = d[word]
        i = (i + 1) % n

    return word

# Modulos can also work to "wrap around"

assert translate([{"Pikachu": "ピカチュウ"}, {"ピカチュウ": "피카츄"}, {"피카츄": "Pikachu"}], 1, "ピカチュウ", 2) == "피카츄",translate([{"Pikachu": "ピカチュウ"}, {"ピカチュウ": "피카츄"}, {"피카츄": "Pikachu"}], 1, "ピカチュウ", 2)
assert translate([{"Pikachu": "ピカチュウ"}, {"ピカチュウ": "피카츄"}, {"피카츄": "Pikachu"}], 1, "ピカチュウ", 0) == "Pikachu", translate([{"Pikachu": "ピカチュウ"}, {"ピカチュウ": "피카츄"}, {"피카츄": "Pikachu"}], 1, "ピカチュウ", 0)