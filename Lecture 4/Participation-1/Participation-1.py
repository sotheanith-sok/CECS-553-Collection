from skimage import color
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

img = io.imread("./colorful rocks.jpg")

# Prompt: top 20% crop + 50% of the right side change value 1

# crop 20 % from the top
img = img[int(0.20 * np.shape(img)[0]) :, :, :]

# Change 50% of the right side to value 1
img[:, int(0.50 * np.shape(img)[1]) :, :] = 1

# Show the image
plt.figure()
plt.imshow(img)
plt.show()
