# Title: Programming Assignment 2
# Due date: Wednesday, September 9, 2021 at 11:59pm
# Author: Sotheanith Sok
# Description:
#  1. Segment the given rocks in “colorful rocks 2.jpg” image
#  2. Plot the result and then save the resulting image as png.
#  3. Count the total number of the gray rocks in the image and print the result.
#  4. Calculate the area of each gray rock and save the result in a file. Explain how you did that.
#  5. Estimate the center of each gray rock and plot the image with red stars on the calculated centers. Explain how you found the centers.
#  6. Upload a pdf file of your code, your answers to question 4 and 5, and the resulting images.

# ------------------------------------------------------------------------------
# Imports
from skimage import color, io
import matplotlib.pyplot as plt
import numpy as np
from im2bw import im2bw
from bwareaopen import bwareaopen
from bwlabeln import bwlabeln

# Load the image and normalize it between 0 and 1
image = io.imread("./colorful rocks 2.jpg")

# Convert image to binary image
image = im2bw(image, 0.72)

# Inverse 0 and 1 with each other for bwareopen and bwlabeln functions
image = np.subtract(1, image)

# Remove all connected components that has less than 800 pixels 
image = bwareaopen(image, 800)

#Label connect components
image = bwlabeln(image)

print(np.unique(image, return_counts = True))

# Show the image
plt.figure()
plt.imshow(image, cmap="gray")
plt.show()
