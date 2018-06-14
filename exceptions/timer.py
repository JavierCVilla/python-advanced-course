from time import time
from contextlib import contextmanager

class mytime:
    pass

@contextmanager
def timer():
    result = mytime()
    start = time()
    yield result
    result.time = time() - start
