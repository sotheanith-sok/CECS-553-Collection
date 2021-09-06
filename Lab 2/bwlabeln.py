# Title: Programming Assignment 2
# Due date: Wednesday, September 9, 2021 at 11:59pm
# Author: Sotheanith Sok
# Description: Label connected components starting from 1. 
# ------------------------------------------------------------------------------
# imports
import numpy as np


def bwlabeln(BW):
    # Labeling connected components
    rows = np.shape(BW)[0]
    cols = np.shape(BW)[1]
    tag = 2
    for row in range(rows):
        for col in range(cols):
            if BW[row, col] == 1:
                BW = _flooding_labeling(BW, row, col, tag)
                tag = tag + 1

    # Adjust labeling so that it starts with 1
    BW = np.subtract(BW, 1)
    BW[BW == -1] = 0

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
