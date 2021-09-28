from scipy import misc
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as py
import numpy as np


img = misc.ascent()


a = gaussian_filter(img,sigma=0.5)
b = gaussian_filter(img,sigma=2)

c = a-b
c[c<0]=0

f, axarr = py.subplots(1,3)
axarr[0].axis('off')
axarr[1].axis('off')
axarr[2].axis('off')
axarr[0].imshow(a,cmap='gray')
axarr[1].imshow(b,cmap='gray')
axarr[2].imshow(c,cmap='gray')


py.show()