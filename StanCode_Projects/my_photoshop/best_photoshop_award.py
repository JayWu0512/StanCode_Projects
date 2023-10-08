"""
File: best_photoshop_award.py
Name: Jay
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.19 #1.25

# Controls the upper bound for black pixel
BLACK_PIXEL = 45  #120


def main():
    """
    創作理念：StanCode is GOD。
    """
    fg = SimpleImage('image_contest/Jay.jpg')
    bg = SimpleImage('image_contest/god_light.png')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(bg.width):
        for y in range(bg.height):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            total = pixel_me.red + pixel_me.blue + pixel_me.green
            if pixel_me.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
