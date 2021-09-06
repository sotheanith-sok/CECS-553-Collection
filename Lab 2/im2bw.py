# Title: Programming Assignment 2
# Due date: Wednesday, September 9, 2021 at 11:59pm 
# Author: Sotheanith Sok
# Description: Converts the grayscale image I to binary image BW, by replacing all pixels in the input image with luminance greater than level with the value 1 (white) and replacing all other pixels with the value 0 (black). 
# ------------------------------------------------------------------------------
# imports
import numpy as np
from skimage import color


def im2bw(I, level):
    # Check image should be converted to grayscale
    if len(np.shape(I)) == 3:
        I = color.rgb2gray(I)

    # Convert a grayscale image to a binary image
    if len(np.shape(I)) < 3:
        I[I > level] = 1
        I[I <= level] = 0
    else:
        print("Error: Image isn't grayscale")
    return I
