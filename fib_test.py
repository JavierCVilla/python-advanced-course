from fib import fib

# old examples

#def test_fib_of_zero():
#    assert fib(0) == 0

#def test_fib_of_one():
#    assert fib(1) == 1

#def test_examples():
#    for q, a in ((0,0),
#		 (1,1),
#		 (2,1)):
#        assert fib(q) == a

from pytest import mark

parametrize = mark.parametrize

from hypothesis import given
from hypothesis.strategies import integers
from hypothesis            import example 


@given(integers(min_value=2, max_value=10000))
@example(20)
def test_fib_equals_sum_of_previous(n):
    assert fib(n) == fib(n-1) + fib(n-2)

@parametrize('q, a',
             ((0,0),
              (1,1),
              (2,1),
              (3,2),
              (4,3),
              (5,5),
              (6,8),
             ))
def test_examples_parametrize(q, a):
    assert fib(q) == a
