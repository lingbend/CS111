class Sand:

    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return f'Sand({self.x},{self.y})'

    def is_move_ok(self, x_to, y_to):
        """
        Check if it is possible to move a piece of sand from (x_from, y_from)
        to (x_to, y_to). Return True if this is possible, False otherwise.

        Assume there is sand at (x_from, y_from) and this location is in bounds. For
        a move to be OK:

        (1) the destination must be in bounds,
        (2) the destination must be empty, and
        (3) the move must not violate the corner rule.

        The corner rule states that for a down-right or down-left move, the
        cell above the destination must be empty.
        >>> from Grid import Grid
        >>> chicken = Sand(Grid.build([[None, 's',   'r'], [None, None, None]]), 1, 0)
        >>> chicken.is_move_ok(1, 1)  # down ok
        True
        >>> chicken.grid = Grid.build([[None, 's', 'r', 's', None], ['r', 'r', 'r', 'r', 'r']])
        >>> chicken.is_move_ok(0, 1)
        False
        >>> chicken.is_move_ok(2, 1)
        False
        >>> chicken.x = 3
        >>> chicken.is_move_ok(5, 1)
        False
        >>> chicken.is_move_ok(2, 1)
        False
        >>> chicken.grid.array[1] = [None, 'r', None, 'r', None]
        >>> chicken.x = 1
        >>> chicken.is_move_ok(0, 1)
        True
        >>> chicken.is_move_ok(2, 1)
        False
        >>> chicken.is_move_ok(1, 1)
        False
        >>> chicken.grid.array[0] = ['r', 's', 'r', 's', 'r']
        >>> chicken.is_move_ok(0, 1)
        False
        >>> chicken.is_move_ok(2, 1)
        False
        >>> chicken.grid.array[1][1] = None
        >>> chicken.is_move_ok(1, 1)
        True
        """

        if (0 <= x_to <= self.grid.width - 1) and (0 <= y_to <= self.grid.height - 1):
            if self.grid.get(x_to, y_to) is None:
                if ((x_to == self.x) or (self.grid.get(x_to, self.y) is None)):
                    return True
        return False

    def gravity(self):
        """
        Given a grid and a coordinate (x, y) that is in bounds, check if there is
        sand at this coordinate. If there is, try to make one move, trying them
        in this order:

        (1) move down, (2) move down-left, (3) move down-right.

        Return the grid in all cases.
        >>> from Grid import Grid
        >>> chicken = Sand(Grid.build([[None, 's', None], [None, None, None]]), 1, 0)
        >>> # down
        >>> chicken.gravity()
        (1, 1)
        >>> chicken.grid = Grid.build([[None, 's', None], [None, 'r', None]])
        >>> chicken.gravity()
        (0, 1)
        >>> chicken.grid = Grid.build([[None, 's', None], ['r', 'r', None]])
        >>> chicken.gravity()
        (2, 1)
        >>> chicken.grid = Grid.build([['r', 's', 'r'], [None, None, None]])
        >>> chicken.gravity()
        (1, 1)
        >>> chicken.grid = Grid.build([['r', None, 'r'], [None, 's', None]])
        >>> chicken.gravity()

        """
        if self.is_move_ok(self.x, self.y + 1):
            return (self.x, (self.y + 1))
        elif self.is_move_ok(self.x - 1, self.y + 1):
            return ((self.x - 1), (self.y + 1))
        elif self.is_move_ok(self.x + 1, self.y + 1):
            return ((self.x + 1), (self.y + 1))
        return None

    def move(self, physics):
        if physics():
            x, y = physics()
            self.grid.set(self.x, self.y, None)
            self.x = x
            self.y = y
            self.grid.set(x, y, self)
        else:
            return