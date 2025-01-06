from pair import *
from operator import mul, sub, add, truediv

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


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
    (Pair('+', Pair(1, Pair(1, nil))), 5)
    >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
    (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == '(':
        pair = tokens[index + 1]
        if index != 0:
            pair_list, index = parse_tokens(tokens, index + 2)
            pair = Pair(pair, pair_list)
        else:
            index += 2
        second_pair, index = parse_tokens(tokens, index)
        return Pair(pair, second_pair), index
    elif tokens[index] == ')':
        return nil, index + 1
    else:
        try:
            if '.' in tokens[index]:
                token = float(tokens[index])
            else:
                token = int(tokens[index])
            pair_list, index = parse_tokens(tokens, index + 1)
            return Pair(token, pair_list), index
        except:
            raise TypeError


def parse(tokens):
    parsed_tokens, index = parse_tokens(tokens, 0)
    return parsed_tokens

def reduce(func, operands, initial):
    if operands == nil:
        return 0
    elif operands.rest == nil:
        return func(initial, operands.first)
    else:
        return reduce(func, operands.rest, func(initial, operands.first))


def apply(operator, operands):
    if operator == '+':
        return reduce(add, operands, 0)
    elif operator == '*':
        return reduce(mul, operands, 1)
    elif operator == '-':
        return reduce(sub, operands.rest, operands.first)
    elif operator == '/':
        return reduce(truediv, operands.rest, operands.first)
    else:
        raise TypeError


def eval(syntax_tree):
    if type(syntax_tree) == int or type(syntax_tree) == float:
        return syntax_tree
    elif type(syntax_tree) == Pair:
        if type(syntax_tree.first) == Pair:
            first = eval(syntax_tree.first)
            rest = syntax_tree.rest.map(eval)
            return Pair(first, rest)
        elif type(syntax_tree.first) == str and syntax_tree.first in '+-/*':
            rest = syntax_tree.rest.map(eval)
            return apply(syntax_tree.first, rest)
    raise TypeError

def main():
    print('Welcome to the CS 111 Calculator Interpreter.')
    while True:
        prompt = input('calc >> ')
        if prompt == 'exit':
            break
        try:
            tokens = tokenize(prompt)
            parsed_tokens = parse(tokens)
            result = eval(parsed_tokens)
            # print(tokens)
            # print(parsed_tokens)
            print(result)
        except Exception as e:
            print(e)
    print('Goodbye!')

if __name__ == '__main__':
    main()