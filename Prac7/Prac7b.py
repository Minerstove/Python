def increased_by(a, seq):
    yield from (i + a for i in seq)

assert [*increased_by(10, (3, 1, 4))] == [13, 11, 14], [*increased_by(10, (3, 1, 4))]
print(*increased_by(10, iter((3, 1, 4))))
