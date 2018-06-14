class myraises:
    def __init__(self, exception_spec):
        self._spec = exception_spec

    def __enter__(self):
        pass

    def __exit__(self, extype, exception, tb):
        # make sure returned exception is the specified one
        if isinstance(exception, self._spec):
            return True
        raise AssertionError("Wrong type of exception raised. Must be {}"
                .format(self._spec))

from contextlib import contextmanager

@contextmanager
def myraises_generator(spec):
    pass
    try:
        yield
    except spec:
        return True
    except:
        assert False
        #we could also raise an exception
    else:
        assert False
