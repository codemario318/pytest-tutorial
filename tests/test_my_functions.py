import time

import pytest
import source.my_functions as mf


def test_add():
    result = mf.add(1, 4)
    assert result == 5


def test_add_string():
    result = mf.add('qwer', 'tyuiop')
    assert 'qwertyuiop'

def test_divide():
    result = mf.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        mf.divide(10, 0)


def test_divide_with_check_zero():
    # Fail: with pytest.raises(ZeroDivisionError):
    with pytest.raises(ValueError):
        mf.divide_with_check_zero(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    r = mf.divide(10, 5)
    assert r == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert mf.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    mf.divide(4, 0)
