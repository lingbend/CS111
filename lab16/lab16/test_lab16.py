from byu_pytest_utils import max_score, with_import


@max_score(2)
@with_import('lab16', 'tokenize')
def test_tokenize_1(tokenize):
    assert tokenize('(+ 3 2)') == ['(', '+', '3', '2', ')']


@max_score(2)
@with_import('lab16', 'tokenize')
def test_tokenize_2(tokenize):
    assert tokenize('(+ 3  2 )') == ['(', '+', '3', '2', ')']


@max_score(2)
@with_import('lab16', 'tokenize')
def test_tokenize_3(tokenize):
    assert tokenize('(- 9 3 3)') == ['(', '-', '9', '3', '3', ')']


@max_score(2)
@with_import('lab16', 'tokenize')
def test_tokenize_4(tokenize):
    assert tokenize('(+ 10 100)') == ['(', '+', '10', '100', ')']


@max_score(2)
@with_import('lab16', 'tokenize')
def test_tokenize_5(tokenize):
    assert tokenize('(+ 5.5 10.5)') == ['(', '+', '5.5', '10.5', ')']


@max_score(5)
@with_import('lab16', 'tokenize')
def test_tokenize_6(tokenize):
    assert tokenize(
        '(* (- 8 4) 4)') == ['(', '*', '(', '-', '8', '4', ')', '4', ')']


@max_score(5)
@with_import('lab16', 'tokenize')
def test_tokenize_7(tokenize):
    assert tokenize('(* (- 6 8) (/ 18 3) (+ 10 1 2))') == [
        '(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
