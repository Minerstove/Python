# pyright: strict

from lab01d import min_to_pass

def test_min_to_pass():
    assert min_to_pass([60]) == 60
    assert min_to_pass((10, 20, 30)) == -1

    # TODO add more tests here
