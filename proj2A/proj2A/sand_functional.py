"""
code taken from a project at Stanford CS106A
"""

import datetime
import tkinter
from Grid import Grid
import doctest


def is_move_ok(grid, x_from, y_from, x_to, y_to):
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
    :param grid: a grid with rocks and sand
    :param x_from: x coordinate of a cell with sand in it
    :param y_from: y coordinate of a cell with sand in it
    :param x_to: x coordinate of a cell to move the sand to
    :param y_to: y coordinate of a cell to move the sand to
    :return True or False
    >>> grid = Grid.build([[None, 's',   'r'], [None, None, None]])
    >>> is_move_ok(grid, 1, 0, 1, 1)  # down ok
    True
    >>> grid = Grid.build([[None, 's', 'r', 's', None], ['r', 'r', 'r', 'r', 'r']])
    >>> is_move_ok(grid, 1, 0, 0, 1)
    False
    >>> is_move_ok(grid, 1, 0, 2, 1)
    False
    >>> is_move_ok(grid, 3, 0, 5, 1)
    False
    >>> is_move_ok(grid, 3, 0, 2, 1)
    False
    >>> grid.array[1] = [None, 'r', None, 'r', None]
    >>> is_move_ok(grid, 1, 0, 0, 1)
    True
    >>> is_move_ok(grid, 1, 0, 2, 1)
    False
    >>> is_move_ok(grid, 1, 0, 1, 1)
    False
    >>> grid.array[0] = ['r', 's', 'r', 's', 'r']
    >>> is_move_ok(grid, 1, 0, 0, 1)
    False
    >>> is_move_ok(grid, 1, 0, 2, 1)
    False
    >>> grid.array[1][1] = None
    >>> is_move_ok(grid, 1, 0, 1, 1)
    True
    """

    if (0 <= x_to <= grid.width - 1) and (0 <= y_to <= grid.height - 1):
        if grid.get(x_to, y_to) is None:
            if (y_to == y_from) or (x_to == x_from) or (grid.get(x_to, y_to - 1) is None):
                return True
    return False


def do_move(grid, x_from, y_from, x_to, y_to):
    """
    Move the sand from (x_from, y_from) to (x_to, y_to) and return the
    resulting grid. Assume that this is a legal move: all coordinates are
    in bounds, and (x_to, y_to) is empty.
    (a different function checks that this is a legal move before do_move() is called)
    :param grid: a grid with rocks and sand
    :param x_from: x coordinate of a cell with sand in it
    :param y_from: y coordinate of a cell with sand in it
    :param x_to: x coordinate of a cell to move the sand to
    :param y_to: y coordinate of a cell to move the sand to
    :return a modified grid
    """
    grid.set(x_from, y_from, None)
    grid.set(x_to, y_to, 's')
    return grid


def do_gravity(grid, x, y):
    """
    Given a grid and a coordinate (x, y) that is in bounds, check if there is
    sand at this coordinate. If there is, try to make one move, trying them
    in this order:

    (1) move down, (2) move down-left, (3) move down-right.

    Return the grid in all cases.
    :param grid: a grid with rocks and sand
    :param x: x coordinate to check
    :param y: y coordinate to check
    :return a modified grid
    >>> # not sand
    >>> grid1 = Grid.build([[None, 's', None], [None, None, None]])
    >>> do_gravity(grid1, 0, 0).array
    [[None, 's', None], [None, None, None]]
    >>> do_gravity(grid1, 1, 1).array
    [[None, 's', None], [None, None, None]]
    >>> # down
    >>> grid2 = Grid.build([[None, 's', None], [None, None, None]])
    >>> do_gravity(grid2, 1, 0).array
    [[None, None, None], [None, 's', None]]
    >>> grid2 = Grid.build([[None, 's', None], [None, 'r', None]])
    >>> do_gravity(grid2, 1, 0).array
    [[None, None, None], ['s', 'r', None]]
    >>> grid2 = Grid.build([[None, 's', None], ['r', 'r', None]])
    >>> do_gravity(grid2, 1, 0).array
    [[None, None, None], ['r', 'r', 's']]
    >>> grid3 = Grid.build([['r', 's', 'r'], [None, None, None]])
    >>> do_gravity(grid3, 1, 0).array
    [['r', None, 'r'], [None, 's', None]]
    >>> grid3 = Grid.build([['r', None, 'r'], [None, 's', None]])
    >>> do_gravity(grid3, 1, 1).array
    [['r', None, 'r'], [None, 's', None]]
    """
    if grid.get(x, y) == 's':
        if is_move_ok(grid, x, y, x, y + 1):
            grid = do_move(grid, x, y, x, y + 1)
        elif is_move_ok(grid, x, y, x - 1, y + 1):
            grid = do_move(grid, x, y, x - 1, y + 1)
        elif is_move_ok(grid, x, y, x + 1, y +1):
            grid = do_move(grid, x, y, x + 1, y + 1)
    return grid


def do_whole_grid(grid):
    """
    Do one round of gravity over the whole grid.

    :param grid: a grid of rock and sand
    :return a modified grid
    >>> grid4 = Grid.build([['s', 's', 's'], [None, None, None], [None, None, None]])
    >>> do_whole_grid(grid4).array
    [[None, None, None], ['s', 's', 's'], [None, None, None]]
    >>> grid5 = Grid.build([['s', 's', 's'], [None, 'r', None], [None, None, None]])
    >>> do_whole_grid(grid5).array
    [[None, 's', None], ['s', 'r', 's'], [None, None, None]]
    """
    for y in reversed(range(grid.height)):
        for x in range(grid.width):
            grid = do_gravity(grid, x, y)
    return grid


#########################################################

"""
Down here is not especially pretty code to set up the GUI,
handle the controls, and draw the grid to the screen.

Don't write any code below here.

"""


def draw_grid_canvas(grid, canvas, scale):
    """
    Draw grid to tk canvas, erasing and then filling it.
    This was ultimately the best performing approach.
    scale is pixels per block
    """
    # pixel size of canvas
    c_width = grid.width * scale + 2
    c_height = grid.height * scale + 2

    canvas.delete('all')

    # draw black per spot
    for y in range(grid.height):
        for x in range(grid.width):
            val = grid.get(x, y)
            if val:
                if val == 'r':
                    color = 'black'
                else:
                    color = 'yellow'
                rx = 1 + x * scale
                ry = 1 + y * scale
                canvas.create_rectangle(
                    rx, ry, rx + scale, ry + scale, fill=color, outline='black')

    canvas.create_rectangle(0, 0, c_width-1, c_height-1, outline='blue')
    canvas.update()


fps_enable = True
fps_count = 0
fps_start = 0


def fps_update():
    global fps_enable, fps_count, fps_start, fps_label
    if not fps_enable:
        return
    fps_count += 1
    if fps_count == 40:
        now = datetime.datetime.now().timestamp()
        delta = now - fps_start
        fps_start = now
        fps = int(1 / (delta / fps_count))
        # print(fps)
        fps_label.config(text=str(fps))
        fps_count = 0


# Global pointers to GUI elements we need in various callbacks
gravity = None
content = None
fps_label = None

SHIFT = 6


# provided function to build the GUI
def make_gui(top, width, height):
    """
    Set up the GUI elements for the Sand window, returning the Canvas to use.
    top is TK root, width/height is canvas size.
    """

    global gravity, content, fps_label
    gravity = tkinter.IntVar()
    content = tkinter.StringVar()

    top.title('Sand')

    # gravity checkbox
    gcheck = tkinter.Checkbutton(
        top, text='Gravity', name='gravity', variable=gravity)
    gcheck.grid(row=0, column=0, sticky='w')
    gravity.set(1)

    # content variable = state of radio button
    sand = tkinter.Radiobutton(top, text="Sand", variable=content, value='s')
    sand.grid(row=0, column=2, sticky='w')

    rock = tkinter.Radiobutton(top, text="Rock", variable=content, value='r')
    rock.grid(row=0, column=3, sticky='w')

    erase = tkinter.Radiobutton(
        top, text="Erase", variable=content, value='erase')
    erase.grid(row=0, column=4, sticky='w')

    bigerase = tkinter.Radiobutton(
        top, text="BigErase", variable=content, value='bigerase')
    bigerase.grid(row=0, column=5, sticky='w')

    content.set('s')

    # ugh 'fg' not a great name for this!
    fps_label = tkinter.Label(top, text="0", fg='lightgray')
    fps_label.grid(row=0, column=6, sticky='w')

    # canvas for drawing
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')

    canvas.xview_scroll(SHIFT, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(SHIFT, "units")

    canvas.grid(row=1, columnspan=12, sticky='w', padx=20, ipady=5)

    top.update()
    return canvas


def big_erase(grid, x, y, canvas, scale):
    """Erase big red circle in the given grid centered on x,y"""
    rad = 4
    # Compute circle around x,y in grid coords
    x1 = x - rad  # this can be out of bounds
    y1 = y - rad

    x2 = x + rad
    y2 = y + rad

    # Draw a red circle .. will be erased by later updates
    # Need to be consistent about grid -> pixel mapping
    canvas.create_oval(1 + x1 * scale, 1 + y1 * scale, 1 + x2 * scale, 1 + y2 * scale,
                       fill='red', outline='')
    canvas.update()

    for ey in range(y1, y2 + 1):
        for ex in range(x1, x2 + 1):
            # circle around x,y
            if grid.in_bounds(ex, ey) and abs(x-ex)**2 + abs(y-ey)**2 <= rad ** 2:
                grid.set(ex, ey, None)


def start_timer(top, speed, fn):
    """Start the my_timer system, calls given fn"""
    top.after(speed, lambda: my_timer(top, speed, fn))


def my_timer(top, speed, fn):
    """my_timer callback, re-posts itself."""
    fn()
    top.after(speed, lambda: my_timer(top, speed, fn))


def sand_action(grid, canvas, scale):
    """This function runs on timer for all periodic tasks."""
    global gravity
    global mouse_fn

    if mouse_fn:
        mouse_fn()

    if gravity.get():
        new_grid = do_whole_grid(grid)
        for y in range(grid.height):
            for x in range(grid.width):
                grid.set(x, y, new_grid.get(x, y))
    draw_grid_canvas(grid, canvas, scale)
    fps_update()


# global mouse sand_action function pointer
# set on mouse down, cleared on mouse-up
mouse_fn = None


def do_mouse_up(event):
    global mouse_fn
    mouse_fn = None


def do_mouse(event, grid, scale, canvas):
    """Callback for mouse click/move"""
    global mouse_fn
    def mouse_fn(): return do_mouse(event, grid, scale, canvas)

    x = (event.x - SHIFT // 2) // scale
    y = (event.y - SHIFT // 2) // scale
    if grid.in_bounds(x, y):
        global content
        val = content.get()  # 's' 'r' None
        if val == 's' or val == 'r':
            grid.set(x, y, val)
        elif val == 'erase':
            grid.set(x, y, None)
        elif val == 'bigerase':
            big_erase(grid, x, y, canvas, scale)
    # print('click', event.x, event.y)


# (provided)
def main():
    import argparse

    # setup the argument parser
    parser = argparse.ArgumentParser(description="Run Conway's game of life")
    parser.add_argument('--width', type=int, default=50,
                        help='width of the board, 50 by default')
    parser.add_argument('--height', type=int, default=50,
                        help='height of the board, 50 by default')
    parser.add_argument('--speed', type=int, default=1,
                        help='speed of each round, 1ms by default')
    parser.add_argument('--scale', type=int, default=10,
                        help='scale of board, 10 by default')

    # parse the command line arguments
    args = parser.parse_args()

    top = tkinter.Tk()
    canvas = make_gui(top, args.width * args.scale +
                      2, args.height * args.scale + 2)
    grid = Grid(args.width, args.height)

    canvas.bind("<B1-Motion>", lambda evt: do_mouse(evt,
                grid, args.scale, canvas))
    canvas.bind("<Button-1>", lambda evt: do_mouse(evt,
                grid, args.scale, canvas))
    canvas.bind("<ButtonRelease-1>", lambda evt: do_mouse_up(evt))

    start_timer(top, args.speed, lambda: sand_action(grid, canvas, args.scale))

    tkinter.mainloop()


if __name__ == '__main__':
    main()
