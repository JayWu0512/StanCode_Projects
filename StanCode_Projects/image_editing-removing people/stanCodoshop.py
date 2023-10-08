"""
File: stanCodoshop.py
Name: Jay Wu
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # calculate color distance
    color_distance = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)

    # return as value
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # get sum and lens, so it can calculate average
    len_pixels = len(pixels)
    red_sum = sum(pixel.red for pixel in pixels)
    green_sum = sum(pixel.green for pixel in pixels)
    blue_sum = sum(pixel.blue for pixel in pixels)

    # calculate average for RGB
    red_avg = red_sum // len_pixels
    green_avg = green_sum // len_pixels
    blue_avg = blue_sum // len_pixels

    # return as list
    return [red_avg, green_avg, blue_avg]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # use tuple to show the list
    avg_rgb = get_average(pixels)
    red_avg, green_avg, blue_avg = avg_rgb

    # set the original value, use infinite and it will be changed to smaller distance later
    min_distance = float('inf')
    best_pixel = 0

    # get every best pixel
    for pixel in pixels:
        distance = get_pixel_dist(pixel, red_avg, green_avg, blue_avg)

        # change best pixel if the one is not the shortest distance
        if distance < min_distance:
            min_distance = distance
            best_pixel = pixel

    # return as value
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    # create blank image
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # put every best pixel into blank image
    for x in range(width):
        for y in range(height):
            pixel_list = [image.get_pixel(x, y) for image in images]
            best_pixel = get_best_pixel(pixel_list)
            result.set_pixel(x, y, best_pixel)

    # Write code to populate image and create the 'ghost' effect

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
