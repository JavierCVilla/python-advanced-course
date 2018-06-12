from secret import xxx
from hypothesis import given
from hypothesis.strategies import integers 
from hypothesis import example

def test_simple():
    assert xxx(1.1,0) == 1.1

def test_two():
    assert xxx(4, 4) == 8

def test_three():
    assert xxx(0, 1) == 1

def test_four():
    assert xxx(-1, 1) == 0

# conmutative
@given(integers(), integers())
def test_five(a,b):
    assert xxx(a,b) == xxx(b,a) 

# identity
@given(integers())
def test_six(a):
    assert xxx(a,0) == a

# associative
@given(integers(), integers(), integers())
def test_seven(a,b,c):
    assert xxx(xxx(a,b), c) == xxx(a, xxx(b,c))
