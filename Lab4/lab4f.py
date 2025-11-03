def classify_by_standing(y, students):
    standing = {
    "freshman": set(),
    "sophomore": set(),
    "junior": set(),
    "senior": set(),
    "immortal": set(),
    }

    for name, id in students:
        if int(id[:4]) == y:
            standing["freshman"].add(name)
        elif int(id[:4]) == y - 1:
            standing["sophomore"].add(name)
        elif int(id[:4]) == y - 2:
            standing["junior"].add(name)
        elif int(id[:4]) == y - 3:
            standing["senior"].add(name)
        else:
            standing["immortal"].add(name)

    return standing

assert classify_by_standing(2025, (
    ("Alpha", "2022-99999"),
    ("Beta", "2021-11111"),
    ("Charlie", "2025-12345"),
    ("Delta", "2024-31415"),
    ("Echo", "2023-27182"),
    ("Foxtrot", "2000-00000"),
)) == {
    "freshman": {"Charlie"},
    "sophomore": {"Delta"},
    "junior": {"Echo"},
    "senior": {"Alpha"},
    "immortal": {"Beta", "Foxtrot"},
}, classify_by_standing(2025, (
    ("Alpha", "2022-99999"),
    ("Beta", "2021-11111"),
    ("Charlie", "2025-12345"),
    ("Delta", "2024-31415"),
    ("Echo", "2023-27182"),
    ("Foxtrot", "2000-00000"),
))

assert classify_by_standing(2999, ()) == {
    "freshman": set(),
    "sophomore": set(),
    "junior": set(),
    "senior": set(),
    "immortal": set(),
}, classify_by_standing(2999, ())