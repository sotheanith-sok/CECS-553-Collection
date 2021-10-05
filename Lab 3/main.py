from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import dilation, remove_small_objects, label
from utilities import gaussian, roberts

img = io.imread("balloons.jpg")

img = img[:, :, 2]/255.

img = gaussian(img)

img = (img < 0.35).astype(np.int0)

img = dilation(
    img,
    np.array(
        [
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ),
)

img = roberts(img)

img = img > 0
img = remove_small_objects(img)

img = label(img)
print(np.max(img))

plt.imshow(img, cmap="gray")
plt.show()

