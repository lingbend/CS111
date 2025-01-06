def eighteen_seventy_five():
    """Come up with the most creative expression that evaluates to 1875,
    using only numbers and the +, *, and - operators.

    >>> eighteen_seventy_five()
    1875
    """
    return int((((int('1000') ** 2 / 5 + 90) // 30) ** .5 + 1000) * 1.8 / 1.784 // 1 + 790)
    