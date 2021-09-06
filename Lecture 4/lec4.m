% % %  ***********************************************************  
% % %  ***********************************************************  
% % %   Read, Plot, Threshold (Segmentation), Save an image
% % %   Lecture 4, September 1, 2021 
% % %  ***********************************************************    
% % %  ***********************************************************    
clc
clear

im = imread('colorful rocks.jpg');  % Read an image
figure,imshow(im);                  % Plot an image

%% Changing RGB to Gray
imgray = rgb2gray(im);              % Convert image to gray of scale 0-1
imgray = im2double(imgray);         % Changes the unit8 to double
figure, imshow(imgray);

%% Thresholding
level = 0.72;
bw = im2bw(imgray, level);
% figure, 
imshowpair(imgray, bw, 'montage')
% ***********Question***********
% ...
%% Reading another image..
im = imread('duck and balls.jpg');  % Read an image
figure,imshow(im);

%% Changing RGB to Gray
imgray = rgb2gray(im);              % Convert image to gray of scale 0-1
imgray = im2double(imgray);         % Changes the unit8 to double
figure, imshow(imgray);

%% Thresholding
level = 0.5;
bw = im2bw(imgray, level);          % Thresholding: pixels>level => 1, else pixels = 0
% figure, 
imshowpair(imgray, bw,'montage')

%% RGB color space
imRed = im(:,:,1);
imGreen = im(:,:,2);
imBlue = im(:,:,3);

figure, 
subplot(2,2,1), imshow(im);
title('Original img');
subplot(2,2,2), imshow(imRed);
title('Red plane img');
subplot(2,2,3), imshow(imGreen);
title('Green plane img');
subplot(2,2,4), imshow(imBlue);
title('Blue plane img');
%% ******* Another Idea *******
levelr = 0.48;
levelg = 0.33; 
levelb = 0.29; 
bwRed = im2bw(imRed, levelr);
bwGreen = im2bw(imGreen, levelg);
bwBlue = im2bw(imBlue, levelb);
bwfinal = bwRed&bwGreen&bwBlue;     % Accepting the pixels that are all 1s

%figure, 
subplot(2,2,1), imshow(bwRed)
title('Red plane');
subplot(2,2,2), imshow(bwGreen)
title('Green plane');
subplot(2,2,3), imshow(bwBlue)
title('Blue plane');
subplot(2,2,4), imshow(bwfinal)
title('Sum of all planes');

%% Reverse the 0s and 1s
bwcomp = imcomplement(bwfinal); 
figure, imshow(bwcomp);

%% Count the number of objects
nrOfpixels = 20;
objs = bwareaopen(bwcomp,nrOfpixels);  % Remove objects < nrOfpixels
%figure, 
imshowpair(bwcomp, objs, 'montage')
labels = bwlabeln(objs);               % Label the connected components/objects
nrOflabels = max(labels(:))
saveas(gcf,'final result.png')
%% Saving and loading images/.mat files/...
if exist('final.mat','file') ~= 2
    save('final.mat','im','objs', 'nrOflabels') % If size is too large, add '-v7.3' as the last input
else
    load('final.mat')
end

 


