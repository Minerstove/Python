from contextlib import contextmanager

from lab7i import Stage

@contextmanager
def raises_value_error():
    """ context block must raise a ValueError """
    try:
        yield
    except ValueError:
        pass
    else:
        assert False


data = Stage()

data.insert_left('ren')
assert data.get(0) == 'ren'

data.insert_left('gino')
data.insert_right('jem')
assert data.get(0) == 'gino'
assert data.get(1) == 'ren'
assert data.get(2) == 'jem'
with raises_value_error():
    data.get(3)

data.insert_left('carlo')
data.insert_right('kevin')
data.insert_left('kelvin')
assert data.get(1) == 'carlo'
assert data.get(0) == 'kelvin'
assert data.get(5) == 'kevin'
with raises_value_error():
    data.get(-1)
