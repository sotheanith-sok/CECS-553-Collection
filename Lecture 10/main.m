clc
clear
close all

im = imread('flower.png');
imGreen = im(:,:,2);

imEdge = edge(imGreen,'sobel');
imshow(imEdge);
