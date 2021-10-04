% % %  ***********************************************************  
% % %  ***********************************************************  
% % %   Filtering an image using different kernels
% % %   Lecture 10, September 27, 2021 
% % %  ***********************************************************    
% % %  ***********************************************************    
clc
clear
close all

im = imread('rocks.jpg');       % Read an image
figure,imshow(im);              % Plot an image

imGray = rgb2gray(im);          % Convert image to gray 
imGray = im2double(imGray);     % Changes the unit8 to double 
figure, imshow(imGray);

H = fspecial('average');                        % Create a constructor for avg filter
imAve = imfilter(imGray,H);                     % Filter the img using your constructor
figure, imshowpair(imGray, imAve,'montage');

imGaus = imgaussfilt(imGray,4);                 % MATLAB recommends this function instead of imfilter when you want to do Gaussian filter
figure, imshowpair(imGray, imGaus,'montage');

%% Edge detection
bw1 = edge(imGray, 'sobel');            % Find the edges using your choice of filter
bw2 = edge(imGaus, 'sobel');
figure, 
subplot(1,2,1), imshow(bw1)
title('w/o blurring')
subplot(1,2,2), imshow(bw2)
title('w blurring')
%% Dilating and Detecting the boundaries
se90 = strel('line', 2, 90);            % Create vertical structure: type,length,direction
se0 = strel('line', 3, 0);              % Create horizontal structure: type,length,direction 
bwDilated = imdilate(bw2, [se90 se0]);  % Dilate img using se0 and se90
figure, imshowpair(bw2,bwDilated,'montage'), 
title('Dilated image');

[B,L] = bwboundaries(bwDilated,'Noholes');  % Find the contour/boundaries in img
boundary = B{1};
figure, imshow(bwDilated); hold on,
plot(boundary(:,2),boundary(:,1),'g','LineWidth',3);

%% Sharpenning an image
im = imread('shell.jpg');       % Read an image
imGray = rgb2gray(im);          % Convert image to gray 
imGray = im2double(imGray);     % Changes the unit8 to double 
imSharpen = imsharpen(imGray);  % Unsharp masking

figure, subplot(1,2,1), imshow(imGray), title('Original image')
subplot(1,2,2), imshow(imSharpen), title('Sharpen image')

imGaus = imgaussfilt(imGray);       % Guassian filtering
imEdge = imGray - imGaus;
imSharpen2 = 2*imGray + 3*imEdge;   % Or simply write: imSharpen2 = 5*imgray - 3*imGauss
figure, imshowpair(imGray, imSharpen2, 'montage')

