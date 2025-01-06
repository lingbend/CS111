def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    if k != 0:
        number = n
        for i in range(k-1):
            n -= 1
            number *= n
    else:
        number = 1
    return number
    

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    6
    """
    divisor = 1
    modulo = 10
    number = 0
    while modulo <= y:
        number += (y % modulo) // divisor
        divisor *= 10
        modulo *= 10
    number += (y % modulo) // divisor
    divisor *= 10
    modulo *= 10
    return number



###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"


if __name__ == '__main__':
    sum_digits(int(input('Enter a number: ')))