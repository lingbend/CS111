from Grid import Grid
import random


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else '-', end=" ")
        print()
    print()



def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    new_grid = grid.copy()
    modify_grid(new_grid, lambda x, y: new_grid.set(x,y,'r'), chance_of_rock)
    # for y in range(new_grid.height):
    #     for x in range(new_grid.width):
    #         random_num = random.random()
    #         if random_num <= chance_of_rock:
    #             new_grid.array[y][x] = 'r'
    return new_grid


def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    new_grid = grid.copy()
    modify_grid(new_grid, lambda x, y: new_grid.set(x,y,'b'), chance_of_bubbles)
    # for y in range(new_grid.height):
    #     for x in range(new_grid.width):
    #         random_num = random.random()
    #         cell = new_grid.array[y][x]
    #         if random_num <= chance_of_bubbles and cell is None:
    #             new_grid.array[y][x] = 'b'
    return new_grid

# tests


def modify_grid(grid, func, prob):
    """Write a function which can take in a grid, a function
    and a probablily as parameters and updates the grid using
    the function passed in."""
    for y in range(grid.height):
        for x in range(grid.width):
            random_num = random.random()
            cell = grid.get(x, y)
            if random_num <= prob and cell is None:
                func(x, y)
    return grid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    new_grid = grid.copy()
    if y != 0:
        new_grid.set(x, y, None)
        new_grid.set(x, y-1, 'b')
    return new_grid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    new_grid = grid.copy()
    for y in range(new_grid.height):
        for x in range(new_grid.width):
            cell = new_grid.get(x, y)
            if y != 0 and (new_grid.get(x, y-1) is None) and cell == 'b':
                new_grid = bubble_up(grid, x, y)
    return new_grid



def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1

if __name__ == '__main__':
    chicken = Grid(10,10)
    duck = random_rocks(chicken, .5)
    cow = random_bubbles(duck, .5)
    animate_grid(cow, 1)
