from cons import Cons
from pytest import mark
from pytest import raises

parametrize = mark.parametrize

@parametrize('value', range(10))
def test_getitem(value):
    c = Cons(value)
    assert c[0] == value

def cons_from_sequence(data):
    rdata = iter(reversed(data))
    c = None
    for item in rdata:
        c = Cons(item, c)
    return c

example = ('hello',
	   range(10),
	   'banana')

@parametrize('data', example)
def test_getitem_double(data):
    c = cons_from_sequence(data)
    for n, item in enumerate(data):
        assert c[n] == item

@parametrize('data', example)
def test_len(data):
    assert len(cons_from_sequence(data)) == len(data)

def test_iteration():
    c = Cons(12, Cons('banana', Cons(dir)))
    i = iter(c)
    assert next(i) == 12
    assert next(i) == 'banana'
    assert next(i) == dir
    #raises(StopIteration, next, i)
    with raises(StopIteration):
        next(i)
