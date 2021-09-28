clc

im = imread('shell.jpg');
imGray = rgb2gray(im);
imGaus=imgaussfilt(imGray);
imEdge = imGray - imGaus;
imSharpen = 2*imGray + 3*imEdge
imshow(200*imEdge);