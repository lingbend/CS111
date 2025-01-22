
"""
code taken from a project at Stanford CS106A
"""

import datetime
import tkinter

from Grid import Grid


"""Insert the Sand class here"""
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

all_sand = []


def add_sand(grid, x, y):
    """
    Attempt to add a Sand object to grid

    The steps are as follows:

    (1) Verify that the position specified by the x & y coordinates is empty in the grid. If not, exit.
    (2) Create a new Sand object and set its position to the supplied x and y coordinates.
    (3) Add the new object to the all_sand list.
    (4) Store a reference to the new object in the correct grid position
    :param grid: a grid with rocks and sand
    :param x: the x coordinate to add sand to
    :param y: the y coordinate to add sand to
    """
    if grid.get(x, y) is None:
        new_sand = Sand(grid, x, y)
        all_sand.append(new_sand)
        grid.set(x, y, new_sand)


def remove_sand(grid, x, y):
    """
    Attempt to remove a Sand object from grid

    The steps are as follows:

    (1) Verify that there is a sand particle in the specified position. If not, exit.
    (2) Remove the reference to the Sand object from the grid.
    (3) Remove the Sand object from the all_sand list.
    :param grid: a grid with rocks and sand
    :param x: the x coordinate to remove sand from
    :param y: the y coordinate to remove sand from
    """
    grid_fill = grid.get(x, y)
    if isinstance(grid_fill, Sand):
        grid.set(x, y, None)
        all_sand.remove(grid_fill)


def do_whole_grid():
    """
    Do one round of gravity over the whole grid.
    """
    all_sand.sort(key=lambda particle: (-particle.y, particle.x))
    for sand_block in all_sand:
        sand_block.move(sand_block.gravity)


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
                if isinstance(grid.get(ex, ey), Sand):
                    remove_sand(grid, ex, ey)
                else:
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
        do_whole_grid()
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
        if val == 's':
            if grid.get(x, y) == 'r':
                grid.set(x, y, None)
            add_sand(grid, x, y)
        elif val == 'r':
            if isinstance(grid.get(x, y), Sand):
                remove_sand(grid, x, y)
            grid.set(x, y, val)
        elif val == 'erase':
            if isinstance(grid.get(x, y), Sand):
                remove_sand(grid, x, y)
            else:
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
