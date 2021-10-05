import numpy as np
import math

def convolve(in_arr, kernel ,stride=1, padding=0, padding_mode="edge"):
    #Expand scaler values to tuple
    if(np.isscalar(padding)):
        padding = (padding, padding) #(top & bottom, left & right)
    if(np.isscalar(stride)):
        stride = (stride,stride) #(verticle stride, horizontal stride)

    #Calculate output array size 
    out_arr_height = math.floor((in_arr.shape[0]+2*padding[0]-kernel.shape[0])/stride[0]) + 1
    out_arr_width = math.floor((in_arr.shape[1]+2*padding[1]-kernel.shape[1])/stride[1]) + 1

    #Add padding to input array
    in_arr = np.pad(in_arr, pad_width = ((padding[0],padding[0]),(padding[1],padding[1])), mode = padding_mode)

    #Create output array
    out_arr = np.zeros((out_arr_height, out_arr_width))

    #Perform convolution between input array and kernel
    for h in range(0, out_arr_height):
        for w in range(0,out_arr_width):
            out_arr[h,w] = np.sum(in_arr[h*stride[0]:h*stride[0]+kernel.shape[0], w*stride[1]:w*stride[1]+kernel.shape[1]] * kernel)
            
    return out_arr

def sobel(img):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_x = convolve(img, Gx, padding=1)
    sobel_y = convolve(img, Gy, padding=1)
    img = np.sqrt(sobel_x**2 + sobel_y**2)
    return img

def roberts(img):
    Gx = np.array([[1,0],[0,-1]])
    Gy = np.array([[0,1],[-1,0]])
    roberts_x = convolve(img, Gx, padding=1)
    roberts_y = convolve(img, Gy, padding=1)
    img = np.sqrt(roberts_x**2 + roberts_y**2)
    return img

def _gen_guassian_kernel(length = 5, sigma = 1.0):
    ax = np.linspace(-(length - 1) / 2., (length - 1) / 2., length)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

def gaussian(img, sigma=1.):
    g_kernel = _gen_guassian_kernel(sigma=sigma)
    return convolve(img, g_kernel,padding=2)
