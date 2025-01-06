# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image



# def iron_puzzle(filename):
#     iron_pic = Image(filename)
#     for y in range(iron_pic.height):
#         for x in range(iron_pic.width):
#             pixel = iron_pic.get_pixel(x,y)
#             pixel.red = 0
#             pixel.green = 0
#             pixel.blue *= 10
#     iron_pic.show()
#     return iron_pic


# def west_puzzle(filename):
#     west_pic = Image(filename)
#     for pixel in west_pic:
#         pixel.green = 0
#         pixel.red = 0
#         if pixel.blue < 16:
#             pixel.blue *= 16
#         else:
#             pixel.blue = 0
#     west_pic.show()
#     return west_pic


# def darken(filename, percent):
#     dark_pic = Image(filename)
#     dark_modifier = (1 - percent)
#     for pixel in dark_pic:
#         pixel.blue *= dark_modifier
#         pixel.red *= dark_modifier
#         pixel.green *= dark_modifier
#     dark_pic.show()
#     return dark_pic


    # def grayscale(filename):
    #     gray_pic = Image(filename)
    #     for pixel in gray_pic:
    #         average = 0
    #         average += pixel.red
    #         average += pixel.blue
    #         average += pixel.green
    #         average //= 3
    #         pixel.red = average
    #         pixel.green = average
    #         pixel.blue = average
    #     gray_pic.show()
    #     return gray_pic



# def sepia(filename):
#     sepia_pic = Image(filename)
#     for pixel in sepia_pic:
#         true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
#         true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
#         true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
#         pixel.red = true_red
#         pixel.blue = true_blue
#         pixel.green = true_green
#         if pixel.red > 255:
#             pixel.red = 255
#         if pixel.blue > 255:
#             pixel.blue = 255
#         if pixel.green > 255:
#             pixel.green = 255
#     sepia_pic.show()
#     return sepia_pic


# def create_left_border(filename, weight):
#     old_pic = Image(filename)
#     new_pic = Image.blank(weight + old_pic.width, old_pic.height)
#     for y in range(new_pic.height):
#         for x in range(new_pic.width):
#             new_pixel = new_pic.get_pixel(x,y)
#             if x < weight:
#                 new_pixel.green = 0
#                 new_pixel.red = 0
#                 new_pixel.blue = 255
#             else:
#                 old_pixel = old_pic.get_pixel(x - weight, y)
#                 new_pixel.red = old_pixel.red
#                 new_pixel.green = old_pixel.green
#                 new_pixel.blue = old_pixel.blue
#     new_pic.show()
#     return new_pic


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    old_image = Image(filename)
    new_image = Image.blank(old_image.width + 50, old_image.height + 25)
    for y in range(new_image.height):
        for x in range(new_image.width):
            pixel = new_image.get_pixel(x,y)
            if (y % 2) == 0:
                pixel.blue = 0
                pixel.red = 0
            elif (x % 2) != 0:
                pixel.red = 0
                pixel.green = 0
            else:
                pixel.green = 0
                pixel.blue = 0
    new_image.show()
    return new_image




def copper_puzzle(filename):
    copper_pic = Image(filename)
    for pixel in copper_pic:
        pixel.red = 0
        pixel.green *= 20
        pixel.blue *= 20
    copper_pic.show()

copper_puzzle("test_files/copper.png")
