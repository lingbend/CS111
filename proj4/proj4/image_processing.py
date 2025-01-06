import sys
from byuimage import Image


# def main():
#     # gets image processing mode
#     mode = sys.argv[1]
#     # given the mode, calls the proper image processing function from the dictionary IMAGE_FUNCTIONS
#     global image_functions
#     if validate_command(sys.argv[1:]):
#         image_functions[mode](sys.argv)


def validate_command(input_list):
    # checks if input is in dictionary and command line has enough arguments for the mode
    command_dict = {'-d': 1, '-k': 3, '-s': 2, '-g': 2, '-b': 6, '-f': 2, '-m': 2, '-c': 6, '-y': 5}
    if len(input_list) > command_dict[input_list[0]] and input_list[0] in command_dict:
        return True
    else:
        return False


def display(input_list):
    # shows an image
    Image(input_list[2]).show()


def darken(input_list):
    # for each pixel in the input file multiplies the rgb values by the factor
    filename, output = get_in_out_put(input_list)
    percent = float(input_list[4])
    dark_pic = Image(filename)
    dark_modifier = (1 - percent)
    for pixel in dark_pic:
        pixel.blue *= dark_modifier
        pixel.red *= dark_modifier
        pixel.green *= dark_modifier
    # saves, shows darkened image
    show_save_image(dark_pic, output)


def sepia(filename, output):
    # uses sepia processing algorythm to modify rbg values in input image
    sepia_pic = Image(filename)
    for pixel in sepia_pic:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        pixel.red = true_red
        pixel.blue = true_blue
        pixel.green = true_green
        if pixel.red > 255:
            pixel.red = 255
        if pixel.blue > 255:
            pixel.blue = 255
        if pixel.green > 255:
            pixel.green = 255
    # saves, shows modified image
    show_save_image(sepia_pic, output)


def grayscale(filename, output):
    # gets average rgb value and sets each channel to average
    gray_pic = Image(filename)
    for pixel in gray_pic:
        average = 0
        average += pixel.red
        average += pixel.blue
        average += pixel.green
        average //= 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    # shows, and saves grayscale image
    show_save_image(gray_pic, output)


def make_borders(input_list):
    # Gets an image and creates an image with a border of specified width and color in RGB
    filename, output = get_in_out_put(input_list)
    thickness = int(input_list[4])
    red_val = int(input_list[5])
    green_val = int(input_list[6])
    blue_val = int(input_list[7])
    old_image = Image(filename)
    border_image = Image.blank(old_image.width + (2 * thickness), old_image.height + (2 * thickness))
    for y in range(border_image.height):
        for x in range(border_image.width):
            new_pixel = border_image.get_pixel(x, y)
            # Checks if pixel belongs in border and colors if it is
            if y < thickness or y >= (border_image.height - thickness):
                new_pixel.red = red_val
                new_pixel.green = green_val
                new_pixel.blue = blue_val
            elif x < thickness or x >= (border_image.width - thickness):
                new_pixel.red = red_val
                new_pixel.green = green_val
                new_pixel.blue = blue_val
            else:
                # Maps original image between borders.
                old_pixel = old_image.get_pixel(x - thickness, y - thickness)
                replace_rgb_values(new_pixel, old_pixel)
    # saves, shows bordered image
    show_save_image(border_image, output)


def flipped(filename, output):
    # Gets old image and creates an identical, flipped image
    old_image = Image(filename)
    flipped_image = Image.blank(old_image.width, old_image.height)
    # for each pixel, getting the coordinates, it maps the old image onto the new upsidedown
    for y in range(old_image.height):
        for x in range(old_image.width):
            old_pixel = old_image.get_pixel(x, y)
            # upsidedown means the image height minus the y value (minus 1 to match starting at 0).
            new_pixel = flipped_image.get_pixel(x, flipped_image.height - y - 1)
            replace_rgb_values(new_pixel, old_pixel)
    # saves, shows bordered image
    show_save_image(flipped_image, output)


def mirror(filename, output):
    # Gets old image and creates an identical, mirrored image
    old_image = Image(filename)
    mirrored_image = Image.blank(old_image.width, old_image.height)
    # for each pixel, getting the coordinates, it maps the old image onto the new, mirrored
    for x in range(old_image.width):
        for y in range(old_image.height):
            old_pixel = old_image.get_pixel(x, y)
            # mirrored means the image width minus the x value (minus 1 to match starting at 0).
            new_pixel = mirrored_image.get_pixel(mirrored_image.width - x - 1, y)
            replace_rgb_values(new_pixel, old_pixel)
    # saves, shows bordered image
    show_save_image(mirrored_image, output)


def collage(input_list):
    # gets pictures and variables needed
    pic1 = Image(input_list[2])
    pic2 = Image(input_list[3])
    pic3 = Image(input_list[4])
    pic4 = Image(input_list[5])
    output = input_list[6]
    thickness = int(input_list[7])
    pic_width = pic1.width
    pic_height = pic1.height
    collage_pic = Image.blank((pic_width * 2 + thickness * 3), pic_height * 2 + thickness * 3)
    # draws pictures on collage using upper, right pixel local as starting location
    draw_pic(collage_pic, pic1, thickness, thickness)
    draw_pic(collage_pic, pic2, (thickness * 2 + pic_width), thickness)
    draw_pic(collage_pic, pic3, thickness, (thickness * 2 + pic_height))
    draw_pic(collage_pic, pic4, (thickness * 2 + pic_width), (thickness * 2 + pic_height))
    # draws borders on collage
    draw_borders(collage_pic, thickness, pic_width, pic_height)
    # saves, shows bordered image
    show_save_image(collage_pic, output)


def draw_pic(canvas_pic, source_pic, startx, starty):
    # starting at upper, right corner of the image pastes image from (STARTX, STARTY)
    for y in range(source_pic.height):
        for x in range(source_pic.width):
            old_pixel = source_pic.get_pixel(x, y)
            new_pixel = canvas_pic.get_pixel(startx + x, starty + y)
            replace_rgb_values(new_pixel, old_pixel)


def draw_borders(pic, thickness, pic_width, pic_height):
    # draws 3 horizontal borders starting at the top
    for y in range(thickness * 3):
        if y < thickness:
            draw_y_border(pic, y)
        elif y < thickness * 2:
            draw_y_border(pic, (pic_height + y))
        elif y < thickness * 3:
            draw_y_border(pic, (pic_height * 2 + y))
    # draws 3 vertical borders starting at the top
    for x in range(thickness * 3):
        if x < thickness:
            draw_x_border(pic, x)
        elif x < thickness * 2:
            draw_x_border(pic, (pic_width + x))
        elif x < thickness * 3:
            draw_x_border(pic, (pic_width * 2 + x))


def draw_y_border(pic, y):
    # draws a black horizontal stipe, 1 pixel tall
    for x in range(pic.width):
        pixel = pic.get_pixel(x, y)
        set_pixel_black(pixel)


def draw_x_border(pic, x):
    # draws a black horizontal stripe, 1 pixel tall
    for y in range(pic.height):
        pixel = pic.get_pixel(x, y)
        set_pixel_black(pixel)


def set_pixel_black(pixel):
    # turns a pixel black
    pixel.green = 0
    pixel.red = 0
    pixel.blue = 0


def green_screen(input_list):
    # gets images and variables
    fore_image = Image(input_list[2])
    back_image = Image(input_list[3])
    output = input_list[4]
    threshold = int(input_list[5])
    factor = float(input_list[6])
    # checks each pixel to see if it is green using variables
    for y in range(fore_image.height):
        for x in range(fore_image.width):
            front_pixel = fore_image.get_pixel(x, y)
            back_pixel = back_image.get_pixel(x, y)
            # replaces front pixel with back if front pixel is green
            if detect_green(front_pixel, threshold, factor):
                replace_rgb_values(front_pixel, back_pixel)
    # saves, shows bordered image
    show_save_image(fore_image, output)


def detect_green(pixel, threshold, factor):
    # checks if a pixel's green value is factor more than the average rgb
    # and checks if green value is above a certain threshold
    # if so returns true
    average = (pixel.green + pixel.red + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True


def show_save_image(pic, output):
    # shows and saves an image
    pic.save(output)


def get_in_out_put(input_list):
    # returns the input file name and output file name
    return input_list[2], input_list[3]


def replace_rgb_values(new_pixel, old_pixel):
    # changes a pixel's rgb values into the another pixel's values
    new_pixel.red = old_pixel.red
    new_pixel.green = old_pixel.green
    new_pixel.blue = old_pixel.blue


image_functions = {'-d': display, '-k': darken, '-s': sepia, '-g': grayscale,
                   '-b': make_borders, '-f': flipped, '-m': mirror, '-c': collage, '-y': green_screen}


if __name__ == '__main__':
    main()
