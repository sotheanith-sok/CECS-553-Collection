# Title: Programming Assignment 2
# Due date: Wednesday, September 9, 2021 at 11:59pm
# Author: Sotheanith Sok
# Description: Remove connected components whos area is less than P pixels. Mathlab version of bwareaopen assumes that 1 is connected components and 0 is background.

# ------------------------------------------------------------------------------
# imports
import numpy as np
import sys

sys.setrecursionlimit(3000)


def bwareaopen(BW, P):
    #Labeling connected components
    rows = np.shape(BW)[0]
    cols = np.shape(BW)[1]
    tag = 2
    for row in range(rows):
        for col in range(cols):
            if BW[row, col] == 1:
                BW = _flooding_labeling(BW, row, col, tag)
                tag = tag + 1

    #Remove connected componets that contains less than P pixels. 
    for component in range(2,tag):
        pixels = np.count_nonzero(BW==component)
        if (pixels<P):
            BW[BW==component] = 0
        else:
            BW[BW==component] = 1

    return BW


def _flooding_labeling(BW, row, col, tag):
    if BW[row, col] == 1:
        BW[row, col] = tag
        # Explore neighbors
        # # Top left
        if row > 0 and col > 0:
            BW = _flooding_labeling(BW, row - 1, col - 1, tag)
        # Top
        if row > 0:
            BW = _flooding_labeling(BW, row - 1, col, tag)
        # Top right
        if row > 0 and col < np.shape(BW)[1] - 1:
            BW = _flooding_labeling(BW, row - 1, col + 1, tag)
        # Left
        if col > 0:
            BW = _flooding_labeling(BW, row, col - 1, tag)
        # Right
        if col < np.shape(BW)[1] - 1:
            BW = _flooding_labeling(BW, row, col + 1, tag)
        # Bottom left
        if row < np.shape(BW)[0] - 1 and col > 0:
            BW = _flooding_labeling(BW, row + 1, col - 1, tag)
        # Bottom
        if row < np.shape(BW)[0] - 1:
            BW = _flooding_labeling(BW, row + 1, col, tag)
        # Bottom right
        if row < np.shape(BW)[0] - 1 and col < np.shape(BW)[1] - 1:
            BW = _flooding_labeling(BW, row + 1, col + 1, tag)

    return BW
