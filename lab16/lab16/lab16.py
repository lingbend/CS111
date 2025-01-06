from pair import *


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.
    >>> tokenize("(+ 3 2)")
    ['(', '+', '3', '2', ')']
    >>> tokenize("(- 9 3 3)")
    ['(', '-', '9', '3', '3', ')']
    >>> tokenize("(+ 10 100)")
    ['(', '+', '10', '100', ')']
    >>> tokenize("(+ 5.5 10.5)")
    ['(', '+', '5.5', '10.5', ')']
    >>> expr = "(* (- 8 4) 4)"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '8', '4', ')', '4', ')']
    >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
    >>> tokenize(expr)
    ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    instring = expression
    if instring == '':
        return []
    else:
        instring, outstring = get_token(instring)
        return [instring] + tokenize(outstring)

def get_token(instring):
    if instring[0].isdigit():
        token = ''
        while instring != '' and (instring[0].isdigit() or instring[0] == '.'):
            token += instring[0]
            instring = instring[1:]
        return (token, instring)
    elif instring[0] in '()+-/*':
        return (instring[0], instring[1:])
    else:
        instring = instring[1:]
        return get_token(instring)


# OPTIONAL
def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    # Write your code here


# print(tokenize("(+ 3 2)"))
