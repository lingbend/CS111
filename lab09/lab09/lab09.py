import random
from Grid import Grid


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    if 1 <= int(n) <= 100:
        return True
    else:
        return False

def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    # try:
    #     for i in range(1000):
    #         num = random.randint(1, 101)
    #         if not in_range2(num):
    #             print(False)
    #             print(num)
    # except ValueError as e:
    #     print(f'The number provided, {e}, is out of range.')
    chicken = Grid(4,4)
    chicken.set(2,2,'adfaf')
    print(chicken.get(8, 8))





def in_range2(num):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    if 1 <= int(num) <= 100:
        return True
    else:
        raise ValueError(num)



if __name__ == '__main__':
    main()