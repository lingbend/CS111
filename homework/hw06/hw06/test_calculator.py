from byu_pytest_utils import max_score, with_import
from pair import *
import pytest


@max_score(4)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_1(parse_tokens):
    # (+ 2 3)
    tokens = ['(', '+', '2', '3', ')']

    key = (Pair('+', Pair(2, Pair(3, nil))), 5)
    assert parse_tokens(tokens, 0) == key


@max_score(6)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_2(parse_tokens):
    # (- 5 2 1)
    tokens = ['(', '-', '5', '2', '1', ')']

    key = (Pair('-', Pair(5, Pair(2, Pair(1, nil)))), 6)
    assert parse_tokens(tokens, 0) == key


@max_score(8)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_3(parse_tokens):
    # (* 6 (/ 2 4))
    tokens = ['(', '*', '6', '(', '/', '2', '4', ')', ')']

    key = (Pair('*', Pair(6, Pair(Pair('/', Pair(2, Pair(4, nil))), nil))), 9)
    assert parse_tokens(tokens, 0) == key


@max_score(10)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_4(parse_tokens):
    # (/ (+ 1 (- 5 1)) 0.5)
    tokens = ['(', '/', '(', '+', '1', '(', '-', '5', '1', ')', ')', '0.5', ')']

    key = (Pair('/', Pair(Pair('+', Pair(1,
           Pair(Pair('-', Pair(5, Pair(1, nil))), nil))), Pair(0.5, nil))), 13)
    assert parse_tokens(tokens, 0) == key


@max_score(12)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_5(parse_tokens):
    # (+ (- 9 (* 2 3)) (/ (+ 8 3 (* 2 2)) (- 3.5 0.5)) 2)
    tokens = ['(', '+', '(', '-', '9', '(', '*', '2', '3', ')', ')', '(', '/', '(', '+',
              '8', '3', '(', '*', '2', '2', ')', ')', '(', '-', '3.5', '0.5', ')', ')', '2', ')']

    key = (Pair('+', Pair(Pair('-', Pair(9, Pair(Pair('*', Pair(2, Pair(3, nil))), nil))), Pair(Pair('/', Pair(Pair('+', Pair(8,
           Pair(3, Pair(Pair('*', Pair(2, Pair(2, nil))), nil)))), Pair(Pair('-', Pair(3.5, Pair(0.5, nil))), nil))), Pair(2, nil)))), 31)
    assert parse_tokens(tokens, 0) == key


@max_score(10)
@with_import('calculator', 'parse_tokens')
def test_parse_tokens_error(parse_tokens):
    # (+ 1 a)
    tokens = ['(', '+', '1', 'a', ')']

    with pytest.raises(TypeError):
        parse_tokens(tokens, 0)
