from byu_pytest_utils import max_score, with_import
from functools import cache


@cache
def make_sand_wrapper_class(Sand):
    class SandWrapper(Sand):
        def __init__(self, grid, x=0, y=0):
            super().__init__(grid, x, y)

        def __str__(self):
            return super().__str__()

        def __repr__(self):
            return str(self)

        def __eq__(self, other):
            if isinstance(other, (Sand, SandWrapper)):
                return str(self) == str(other)
            else:
                return False

        def __hash__(self):
            return hash(str(self))

    return SandWrapper


def build_sandy_grid(Grid, Sand, lst):
    SandWrapper = make_sand_wrapper_class(Sand)

    grid = Grid.build(lst)
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == 's':
                grid.set(x, y, SandWrapper(grid, x, y))

    def fancy_grid_toString(self):

        def get_particle_string(obj):
            if isinstance(obj, (Sand, SandWrapper)):
                return "s"
            elif obj == "r":
                return "r"
            elif obj is None:
                return " "
            else:
                return "?"

        assert isinstance(self, Grid), "Either you did this on purpose, or something went horribly wrong"
        s = "\n"  # We lead with a newline to get off a possibly indented line
        for y in range(self.height):
            for x in range(self.width):
                s += "|" + get_particle_string(self.get(x, y))
            s += "|\n"
        return s

    Grid.__str__ = fancy_grid_toString

    return grid


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_str(Grid, Sand):
    grid = Grid(6, 6)
    assert str(Sand(grid, 1, 2)) == 'Sand(1,2)'
    assert str(Sand(grid, 5, 3)) == 'Sand(5,3)'


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_out_of_bounds(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['s']])
    assert (actual := grid.get(0, 0).gravity()) is (expected := None), \
        f"got {actual} instead of {expected} with grid: {grid}"


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_cant_move(Grid, Sand):
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    assert (actual := grid.get(1, 0).gravity()) is (expected := None), \
        f"got {actual} instead of {expected} with grid: {grid}"


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_straight_down(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['s'], [None]])
    assert (actual := grid.get(0, 0).gravity()) == (expected := (0, 1)), \
        f"got {actual} instead of {expected} with grid: {grid}"



@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_down_left(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [[None, 's'], [None, 'r']])
    assert (actual := grid.get(1, 0).gravity()) == (expected := (0, 1)), \
        f"got {actual} instead of {expected} with grid: {grid}"


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_down_right(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['r', 's', None], ['r', 's', None]])
    assert (actual := grid.get(1, 0).gravity()) == (expected := (2, 1)), \
        f"got {actual} instead of {expected} with grid: {grid}"


@max_score(4)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_gravity_corner_rule(Grid, Sand):
    grid = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    assert (actual := grid.get(1, 0).gravity()) is (expected := None), \
        f"got {actual} instead of {expected} with grid: {grid}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_out_of_bounds(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['s']])
    grid = build_sandy_grid(Grid, Sand, [['s']])
    sand = grid.get(0, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_cant_move(Grid, Sand):
    key = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         ['s', 's', 's']]
    )
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_straight_down(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [[None], ['s']])
    grid = build_sandy_grid(Grid, Sand, [['s'], [None]])
    sand = grid.get(0, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_down_left(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [[None, None], ['s', 'r']])
    grid = build_sandy_grid(Grid, Sand, [[None, 's'], [None, 'r']])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_down_right(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['r', None, None], ['r', 's', 's']])
    grid = build_sandy_grid(Grid, Sand, [['r', 's', None], ['r', 's', None]])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(3)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_corner_rule(Grid, Sand):
    key = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    grid = build_sandy_grid(Grid, Sand, [['r', 's', 'r'], [None, 'r', None]])
    sand = grid.get(1, 0)
    sand.move(sand.gravity)
    assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(2)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_falling_example(Grid, Sand):
    keys = [
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, 's', None],
             [None, 's', None],
             ['s', 's', None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', 's']]
        ),
        build_sandy_grid(
            Grid, Sand,
            [[None, None, None],
             [None, None, None],
             [None, None, None],
             [None, 's', None],
             ['s', 's', 's']]
        )
    ]
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, None, None]]
    )
    for key in keys:
        for y in reversed(range(grid.height)):
            for x in range(grid.width):
                elem = grid.get(x, y)
                if isinstance(elem, Sand):
                    elem.move(elem.gravity)
        assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"


@max_score(2)
@with_import('Sand', 'Sand')
@with_import('Grid', 'Grid')
def test_sand_move_antigravity(Grid, Sand):

    def antigravity(self):
        if self.grid.get(self.x, self.y) is self:
            for x_to, y_to in [(self.x, self.y - 1), (self.x - 1, self.y - 1), (self.x + 1, self.y - 1)]:
                try:
                    if self.is_move_ok(x_to, y_to):
                        return x_to, y_to
                except IndexError:
                    pass
        return None
    Sand.antigravity = antigravity

    keys = [
        build_sandy_grid(
            Grid, Sand,
            [[None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, None, None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [['s', 's', None],
             [None, 's', None],
             [None, 's', None],
             [None, None, None],
             [None, None, None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [['s', 's', 's'],
             [None, 's', None],
             [None, None, None],
             [None, None, None],
             [None, None, None]]
        ),
        build_sandy_grid(
            Grid, Sand,
            [['s', 's', 's'],
             [None, 's', None],
             [None, None, None],
             [None, None, None],
             [None, None, None]]
        )
    ]
    grid = build_sandy_grid(
        Grid, Sand,
        [[None, None, None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None],
         [None, 's', None]]
    )
    for key in keys:
        for y in range(grid.height):
            for x in range(grid.width):
                elem = grid.get(x, y)
                if isinstance(elem, Sand):
                    elem.move(elem.antigravity)
        assert grid == key, f"grid does not match key\ngrid:{grid}\nkey:{key}"
