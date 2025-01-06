from lab12 import *
import pytest
from operator import add, mul

# Write your test code here for Q1 and Q2

def test_product():
    assert product(4) == 24
    with pytest.raises(ValueError):
        product(0)
    with pytest.raises(ValueError):
        product(-1)
    with pytest.raises(ValueError):
        product("chicken")
    with pytest.raises(ValueError):
        product(1.0)
    assert product(6) == 720
    assert product(1) == 1

def test_summation():
    assert summation(0) == 0
    assert summation(1) == 1
    assert summation(10) == 55
    assert summation(4) == 10
    with pytest.raises(ValueError):
        summation(-1)
    with pytest.raises(ValueError):
        summation('chicken')
    with pytest.raises(ValueError):
        summation(1.0)

def test_accumulate():
    assert accumulate(add, 0, 5) == 15
    assert accumulate(add, 4, 9) == 49
    assert accumulate(mul, 0, 9) == 0
    assert accumulate(mul, 1, 8) == 40320
    assert accumulate(lambda x, y: y + (x ** 2), 2, 3) == 732
    with pytest.raises(ValueError):
        accumulate(add, 9, 1)
    with pytest.raises(ValueError):
        accumulate(mul, 'chicken', 9)
    with pytest.raises(ValueError):
        accumulate(add, 2, 'chicken')

def test_product_short():
    assert product_short(4) == 24
    with pytest.raises(ValueError):
        product_short(0)
    with pytest.raises(ValueError):
        product_short(-1)
    with pytest.raises(ValueError):
        product_short("chicken")
    with pytest.raises(ValueError):
        product_short(1.0)
    assert product_short(6) == 720
    assert product_short(1) == 1

def test_summation_short():
    assert summation_short(0) == 0
    assert summation_short(1) == 1
    assert summation_short(10) == 55
    assert summation_short(4) == 10
    with pytest.raises(ValueError):
        summation_short(-1)
    with pytest.raises(ValueError):
        summation_short('chicken')
    with pytest.raises(ValueError):
        summation_short(1.0)

# Q3
#####################################

def test_square():
    assert square(0) == 0
    assert square(-1) == 1
    assert square(1) == 1
    assert square(5) == 25
    assert square(3) == 9
    assert square(-5) == 25
    assert square(1.5) == pytest.approx(2.25)


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(25) == 5
    assert sqrt(1) == 1
    assert sqrt(2.5) == pytest.approx(1.58113883)



def test_mean():
    assert mean([0,0,0,0,0,0,]) == 0
    assert mean([-1,-1,-1,-1]) == -1
    assert mean([100, 42, -2, -9] == pytest.approx(32.75))
    assert mean([5]) == 5
    assert mean([1, 1]) == 1


def test_median():
    assert median([1,1,1,1,1,1,1]) == 1
    assert median([0,0,0,0,0]) == 0
    assert median([-1,-1,-1]) == -1
    assert median([55,12,90]) == 12
    assert median([-4, 6, 1, 43, 100, -54, 3, 9, 7, 2, 1]) == 6
    assert median([5, 7, 3, 3, 3]) == 3
    assert median([3, 7, 1, 9]) == 10
    assert median([5, 1, 9, 14]) == 7


def test_mode():
    assert mode([1, 1, 1]) == 1
    assert mode([0,0,0,0,0,0]) == 0
    assert mode([-1,-1,-1,-1,-1]) == -1
    assert mode([3,3,3,3,6,6,6,6,2]) == 3
    assert mode([-53, 4, 9, 5, -53]) == -53
    assert mode([.5, .6, .6, .2, .4, .6]) == pytest.approx(.6)


def test_std_dev():
    """Write your code here"""


def test_stat_analysis():
    """Write your code here"""


# OPTIONAL
#####################################

def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
