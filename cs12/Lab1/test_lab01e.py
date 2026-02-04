# pyright: strict

from lab01e import draw_whirlpool
from oj import Corner, Direction

def test_draw_whirlpool():
    assert draw_whirlpool(Corner.BOTTOM_RIGHT, Direction.UP, 5, 7) == [
        "#######",
        "#.....#",
        "#.###.#",
        "#...#.#",
        "#####.#",
    ]

    # TODO add more tests here
