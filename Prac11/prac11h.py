def print_return(f):
    def _f(*args, **kwargs):
        res = f(*args, **kwargs)
        arg_list = [repr(a) for a in args]
        arg_list += [f"{k}={repr(v)}" for k, v in kwargs.items()]
        arg_str = ", ".join(arg_list)
        print(f"{f.__name__}({arg_str}) = {repr(res)}")
        return res
    return _f
