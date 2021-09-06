from skimage import color, io
import matplotlib.pyplot as plt
import numpy as np

img = io.imread('./duck and balls.jpg')
# img = color.rgb2gray(img)

plt.figure()
plt.imshow(img[:,:,2], cmap=plt.cm.gray)
plt.imshow(img[:,:,2], cmap=plt.cm.gray)
plt.show()