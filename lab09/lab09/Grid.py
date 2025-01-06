class Grid:

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.grid = []
        for i in range(self.height):
            temp_list = []
            for j in range(self.width):
                temp_list.append(None)
            self.grid.append(temp_list)

    def get(self, x, y):
        x = int(x)
        y = int(y)
        try:
            if self.in_bounds(x, y):
                return self.grid[y][x]
        except IndexError as e:
            print('Error, value(s) out of range.')

    def set(self, x, y, val):
        x = int(x)
        y = int(y)
        try:
            if self.in_bounds(x, y):
                self.grid[y][x] = val
            return None
        except IndexError:
            print('Error, value(s) out of range.')


    def in_bounds(self, x, y):
        x = int(x)
        y = int(y)
        if x - 1 <= self.width and y - 1 <= self.height:
            return True
        else:
            raise IndexError

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.grid[0][0]})'

    def __repr__(self):
        return f'Grid({self.height}, {self.width}, first = {self.grid[0][0]})' # update this later

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.grid == other.grid

"""
2D grid with (x, y) int indexed internal storage
Has .width .height size properties
"""