# pyright: strict

from lab01b import move_around

def test_move_around():
    grid = [
        "....",
        ".x#.",
        ".##.",
        "....",
    ]
    moves = "LD"

    assert move_around(grid, moves) == [
        "....",
        ".x..",
        "..#.",
        ".##.",
    ]

    # TODO add more tests here
