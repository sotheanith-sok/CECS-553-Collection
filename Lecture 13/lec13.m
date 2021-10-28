% % %  ***********************************************************  
% % %  ***********************************************************  
% % %   Image Classification Using KNN
% % %   Lecture 13, October 6, 2021 
% % % 
% % %   Note: Images are taken from CIFAR-10
% % %   https://www.kaggle.com/fedesoriano/cifar10-python-in-csv
% % %  ***********************************************************    
% % %  ***********************************************************    
clc
clear
close all

nr_im = 150;
for i = 1:nr_im
   im = imread(['tiny/im', num2str(i), '.png']); %  ****************** Question ****************** Read each image located in tiny folder
   All(:,:,:,i) = im;                           % Save all of the imgs in All
end
All = reshape(All,size(All,1)*size(All,2)*size(All,3),nr_im);  % Change All into a matrix (each row = one img)
% save('TinyIms.mat', 'All', 'nr_im')

% Test to see what has happened...
% im = All(:,1);
% im = reshape(im,32,32,3);
% imshow(im)
%% Read the labels
fileID = fopen('tiny/labels.txt','r');  % Open the txt file for reading
chr = fscanf(fileID,'%c');              % Read data, '%c' = Read any single character
range = sscanf(chr,'%d');               % Convert chr to numbers, '%d' = integers
NrLabels = length(range)/2;

for i = 1:NrLabels
    labels(range(2*i-1):abs(range(2*i)))=i; % ****************** Question ****************** Define a column vector of size nr_im and save the labels for each img/row in All
end

fclose(fileID)                          % Close the file
%% K-Fold Cross Validation
k = 5;
c = cvpartition(nr_im,'KFold',k);       % Define a random partition for k folds


idxTrain = training(c,1);               % Return the training indices for repetition i
idxTest = test(c,1);                    % Return the testing indices for repetition i
TestIDs = find(idxTest == 1);           % Find the acctual index values

disp(sum(c.TrainSize));

nr_test = sum(idxTest);  %****************** Question ****************** Find the total number of test data 
nr_train = sum(idxTrain); %****************** Question ****************** Find the total number of test data

acc = 0;
for i = 1:size(TestIDs,1)
    testId = TestIDs(i);
    testIm = All(:,testId);
    dst = abs(All(:,idxTrain)-repmat(testIm,1,nr_train));   %Calculate the distance between all training imgs and the test img
    dst = sum(dst);
    [~,mnIdx] = mink(dst,k);                 % Find the k smallest elements
    Allids = 1:nr_im;

    testLab = labels(idxTrain);
    lab = testLab(mnIdx);

    vote = mode(lab);      %****************** Question ****************** Find the most frequent value 
    acc = acc + (vote == labels(testId));                 % Check to see if you predicted the label correctly 
end

disp(acc/size(TestIDs,1));