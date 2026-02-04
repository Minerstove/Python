# pyright: strict

from lab01c import display

def test_display():
    assert display(12) == [
        "      -- ",
        "   |    |",
        "      -- ",
        "   | |   ",
        "      -- ",
    ]

    # TODO add more tests here
