from byuimage import Image


def flipped(filename):
    # Gets old image and returns an identical, flipped image
    old_image = Image(filename)
    flipped_image = Image.blank(old_image.width, old_image.height)
    # for each pixel, getting the coordinates, it maps the old image onto the new upsidedown
    for y in range(old_image.height):
        for x in range(old_image.width):
            old_pixel = old_image.get_pixel(x, y)
            # upsidedown means the image height minus the y value (minus 1 to match starting at 0).
            new_pixel = flipped_image.get_pixel(x, flipped_image.height - y - 1)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return flipped_image


def make_borders(filename, thickness, red_val, green_val, blue_val):
    # Gets an image and returns an image with a border of specified width and color in RGB
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
                new_pixel.red = old_pixel.red
                new_pixel.green = old_pixel.green
                new_pixel.blue = old_pixel.blue
    return border_image


if __name__ == '__main__':
    pass
