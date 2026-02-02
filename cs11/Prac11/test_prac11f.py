from contextlib import contextmanager

from prac11f import OneToOneCorrespondence

@contextmanager
def raises_value_error():
    """ context block must raise a ValueError """
    try:
        yield
    except ValueError:
        pass
    else:
        assert False


data = OneToOneCorrespondence(
    ('K', 'J'),
    ('J', 'T'),
    ('O', 'Z'),
    ('L', 'AA'),
    ('M', 'Frank'),
)

assert data.get_left('J') == 'K'
assert data.get_right('J') == 'T'
assert data.get_right('L') == 'AA'
data.set_pair('AA', 'A')
assert data.get_right('AA') == 'A'
data.remove_pair_with_right('Frank')
with raises_value_error():
    data.get_left('Frank')
data.set_pair('Frank', 'M')
with raises_value_error():
    data.set_pair('Frank', 'HighT')
