def sockets_that_match(plug, sockets):
    enumerated_sockets = _enumerate(sockets,0)
    return tuple(i for i,socket in enumerated_sockets if valid_socket_checker(plug, socket))

def _enumerate(tup, start):
    if len(tup) == 0:
        return ()
    return ((start, tup[0]),) + (_enumerate(tup[1:], start + 1))

def valid_socket_checker(plug, socket):
    if len(plug) != len(socket):
        return False
    if all(tuple((plug[i] + socket[i] == plug[0] + socket[0]) for i in range(len(plug)))):
        return True

assert sockets_that_match((1, 2, 1), ((1, 1), (2, 1, 2), (6,), (3, 2, 3))) == (1, 3), sockets_that_match((1, 2, 1), ((1, 1), (2, 1, 2), (6,), (3, 2, 3)))

#DONE
