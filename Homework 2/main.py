from skimage import io, color
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from skimage.filters import threshold_otsu
import numpy as np
from skimage import data

plt.rcParams.update({'font.size': 18})

image_color = io.imread('test.png')
print(np.shape(image_color))
image_grayscale = (color.rgb2gray(image_color)*255.).astype(int)
pixel_intensities, pixel_counts = np.unique(image_grayscale, return_counts=True)
threshold = threshold_otsu(image_grayscale)
image_binary = image_grayscale<=threshold

fig, axes = plt.subplots(nrows=2, ncols=2)

#Color image
axes[0,0].title.set_text('Color Image')
axes[0,0].imshow(image_color)

#Grayscale images
axes[0,1].title.set_text('Grayscale Image')
axes[0,1].imshow(image_grayscale, cmap='gray')


#Histogram
axes[1,0].title.set_text('Histogram')
axes[1,0].set_xlabel('Pixel Intensity')
axes[1,0].set_ylabel('Pixel Count')

#Add threshold to histogram
l = axes[1,0].axvline(x=threshold, color='red', ls='--')
l.set_label('Intensity Threshold')
axes[1,0].text(threshold, 0, threshold, color='red')

#Plot histogram
axes[1,0].plot(pixel_intensities,pixel_counts)
axes[1,0].legend()


#Binary images
axes[1,1].title.set_text('Binary Image')
axes[1,1].imshow(image_binary,cmap='gray')

plt.show()