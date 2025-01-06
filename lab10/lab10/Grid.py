from copy import deepcopy


class Grid:

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.array = []
        for i in range(self.height):
            temp_list = []
            for j in range(self.width):
                temp_list.append(None)
            self.array.append(temp_list)

    def get(self, x, y):
        x = int(x)
        y = int(y)
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            raise IndexError

    def set(self, x, y, val):
        x = int(x)
        y = int(y)
        if self.in_bounds(x, y):
            self.array[y][x] = val
        else:
            raise IndexError
        return None


    def in_bounds(self, x, y):
        x = int(x)
        y = int(y)
        if (0 <= x <= (self.width - 1)) and (0 <= y <= (self.height - 1)):
            return True
        else:
            return False

    def __str__(self):
        return f'Grid({self.height}, {self.width}, first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.array})' # update this later

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        elif not isinstance(other, Grid):
            return False


    @staticmethod
    def check_list_malformed(in_list):
        sub_list_length = None
        if type(in_list) == list and len(in_list) > 0:
            for element in in_list:
                if type(element) == list:
                    if sub_list_length is None or len(element) == sub_list_length:
                        sub_list_length = len(element)
                        continue
                    else:
                        Grid.malformed_exception(in_list)
                else:
                    Grid.malformed_exception(in_list)
        else:
            Grid.malformed_exception(in_list)

    @staticmethod
    def malformed_exception(in_list):
        raise ValueError(f"This input data is not a list or formatted incorrectly: {in_list}")


    @staticmethod
    def build(in_list):
        Grid.check_list_malformed(in_list)
        height = len(in_list)
        width = len(in_list[0])
        new_grid = Grid(width, height)
        new_grid.array = deepcopy(in_list)
        return new_grid


    def copy(self):
        return Grid.build(self.array)



"""
2D grid with (x, y) int indexed internal storage
Has .width .height size properties
"""