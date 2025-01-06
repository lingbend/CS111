from byu_pytest_utils import dialog, max_score, test_files, this_folder, with_import
from operator import add, mul, pow
from pair import *
import pytest


@max_score(2)
@with_import('calculator', 'parse')
def test_parse_1(parse):
    # (+ 2 3)
    tokens = ['(', '+', '2', '3', ')']

    key = Pair('+', Pair(2, Pair(3, nil)))
    assert parse(tokens) == key


@max_score(2)
@with_import('calculator', 'parse')
def test_parse_2(parse):
    # (- 5 2 1)
    tokens = ['(', '-', '5', '2', '1', ')']

    key = Pair('-', Pair(5, Pair(2, Pair(1, nil))))
    assert parse(tokens) == key


@max_score(2)
@with_import('calculator', 'parse')
def test_parse_3(parse):
    # (* 6 (/ 2 4))
    tokens = ['(', '*', '6', '(', '/', '2', '4', ')', ')']

    key = Pair('*', Pair(6, Pair(Pair('/', Pair(2, Pair(4, nil))), nil)))
    assert parse(tokens) == key


@max_score(2)
@with_import('calculator', 'parse')
def test_parse_4(parse):
    # (/ (+ 1 (- 5 1)) 0.5)
    tokens = ['(', '/', '(', '+', '1', '(', '-', '5', '1', ')', ')', '0.5', ')']

    key = Pair('/', Pair(Pair('+', Pair(1,
               Pair(Pair('-', Pair(5, Pair(1, nil))), nil))), Pair(0.5, nil)))
    assert parse(tokens) == key


@max_score(2)
@with_import('calculator', 'parse')
def test_parse_5(parse):
    # (+ (- 9 (* 2 3)) (/ (+ 8 3 (* 2 2)) (- 3.5 0.5)) 2)
    tokens = ['(', '+', '(', '-', '9', '(', '*', '2', '3', ')', ')', '(', '/', '(', '+',
              '8', '3', '(', '*', '2', '2', ')', ')', '(', '-', '3.5', '0.5', ')', ')', '2', ')']

    key = Pair('+', Pair(Pair('-', Pair(9, Pair(Pair('*', Pair(2, Pair(3, nil))), nil))), Pair(Pair('/', Pair(Pair('+', Pair(8,
               Pair(3, Pair(Pair('*', Pair(2, Pair(2, nil))), nil)))), Pair(Pair('-', Pair(3.5, Pair(0.5, nil))), nil))), Pair(2, nil))))
    assert parse(tokens) == key


@max_score(5)
@with_import('calculator', 'parse')
def test_parse_error(parse):
    # (+ 1 a)
    tokens = ['(', '+', '1', 'a', ')']

    with pytest.raises(TypeError):
        parse(tokens)


@max_score(5)
@with_import('calculator', 'reduce')
def test_reduce_1(reduce):
    assert reduce(add, nil, 0) == 0


@max_score(5)
@with_import('calculator', 'reduce')
def test_reduce_2(reduce):
    assert reduce(add, Pair(3, Pair(4, Pair(5, nil))), 0) == 12


@max_score(5)
@with_import('calculator', 'reduce')
def test_reduce_3(reduce):
    assert reduce(mul, Pair(2, Pair(4, Pair(8, nil))), 1) == 64


@max_score(5)
@with_import('calculator', 'reduce')
def test_reduce_4(reduce):
    assert reduce(pow, Pair(1, Pair(2, Pair(3, Pair(4, nil)))), 2) == 16777216


@max_score(4)
@with_import('calculator', 'apply')
def test_apply_1(apply):
    assert apply('+', Pair(2, Pair(3, Pair(4, nil)))) == 9


@max_score(4)
@with_import('calculator', 'apply')
def test_apply_2(apply):
    assert apply('-', Pair(13, Pair(2, Pair(4, Pair(3, nil))))) == 4


@max_score(4)
@with_import('calculator', 'apply')
def test_apply_3(apply):
    assert apply('*', Pair(9, Pair(5, Pair(0.2, nil)))) == 9.0


@max_score(4)
@with_import('calculator', 'apply')
def test_apply_4(apply):
    assert apply('/', Pair(9, Pair(2, nil))) == 4.5


@max_score(4)
@with_import('calculator', 'apply')
def test_apply_error(apply):
    with pytest.raises(TypeError):
        apply('asdf', Pair(2, Pair(3, nil)))


@max_score(2.5)
@with_import('calculator', 'eval')
def test_eval_primitives(eval):
    assert eval(4) == 4
    assert eval(0.3) == 0.3


@max_score(3)
@with_import('calculator', 'eval')
def test_eval_1(eval):
    # (+ 2 3)
    expression = Pair('+', Pair(2, Pair(3, nil)))

    assert eval(expression) == 5


@max_score(3)
@with_import('calculator', 'eval')
def test_eval_2(eval):
    # (- 5 2 1)
    expression = Pair('-', Pair(5, Pair(2, Pair(1, nil))))

    assert eval(expression) == 2


@max_score(3)
@with_import('calculator', 'eval')
def test_eval_3(eval):
    # (* 6 (/ 2 4))
    expression = Pair(
        '*', Pair(6, Pair(Pair('/', Pair(2, Pair(4, nil))), nil)))

    assert eval(expression) == 3.0


@max_score(3)
@with_import('calculator', 'eval')
def test_eval_4(eval):
    # (/ (+ 1 (- 5 1)) 0.5)
    expression = Pair(
        '/', Pair(Pair('+', Pair(1, Pair(Pair('-', Pair(5, Pair(1, nil))), nil))), Pair(0.5, nil)))

    assert eval(expression) == 10.0


@max_score(3)
@with_import('calculator', 'eval')
def test_eval_5(eval):
    # (+ (- 9 (* 2 3)) (/ (+ 8 3 (* 2 2)) (- 3.5 0.5)) 2)
    expression = Pair('+', Pair(Pair('-', Pair(9, Pair(Pair('*', Pair(2, Pair(3, nil))), nil))), Pair(Pair('/', Pair(Pair('+', Pair(
        8, Pair(3, Pair(Pair('*', Pair(2, Pair(2, nil))), nil)))), Pair(Pair('-', Pair(3.5, Pair(0.5, nil))), nil))), Pair(2, nil))))

    assert eval(expression) == 10.0


@max_score(2.5)
@with_import('calculator', 'eval')
def test_eval_error(eval):
    with pytest.raises(TypeError):
        eval('asdf')


@max_score(25)
@dialog(test_files / 'black_box.dialog.txt', this_folder / 'calculator.py')
def test_interactive_program():
    ...
