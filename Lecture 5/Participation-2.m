image = imread('cells.png');
image = image(:,:,1);
image = im2bw(image,0.1);
image = bwareaopen(image,10);
[L,n] = bwlabeln(image);
disp(n);
imshow(image);