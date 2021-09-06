% % %  ***********************************************************  
% % %  ***********************************************************  
% % %   Arrays, Cell Arrays, For Loops, If conditions, Printing, ...
% % %  ***********************************************************    
% % %  ***********************************************************
clc     % Clear the command window
clear   % Remove the items in workspace
% % doc for %doc = Reference page in Help browser
%% Arrays
x = [1 4 6 8 9 3];
x(2);
a = [1 4 5 7 9 0 2 3];
a(end)       % Prints the last element in the array
a(end) = []; % Delete the last element 
a
length(a)
size(a)
size(a,1)
size(a,2)
% z = zeros(2);
% z = zeros(2,1); 
% one = ones(2,1);
% % ***********************************************************************
% % *********************Adding/subtracting/multiplying/*******************
% a = [10 20 -5; 30 -1 3];
% b = [2 3 4; 1 0 0];
% a+1
% a.*2  % Elementwise multiplication
% a.*b
% a(3,:) = [1 1 1];
% a(1:2,2:end)  % Printing parts of the matrix
% clear a b
% % ***********************************************************************
% % *********************Check whether the array is empty******************
% a = [6 2 4];
%  isempty(a)
%  isempty([])
%% Finding elements in the array
% % Use "doc find" to read the details of find function

% % Print the indices greater than 2 
% a>2
% find(a>2)       % you can use this for a matrix or an array
% [r,c]=find(a>2) % better to use this when you a matrix (not an array)
% B = [1 3 4; 2 -1 4];
% [r,c] = find(B>2);
% [r,c]

% % Print the elements greater than 2 
%a(a>2)     
%a(a>=2)    
%a(a~=1) % not equal to 1
%% Concatenate arrays along some dimension (read more details using "doc cat")
% a = [1 2 3];
% % cat(dim,A,B,C,..) 
% % if dim=2 ==> along the columns// if dim=1 ==> along the rows
% cat(2,a,5000,[-1 -2 -3])

% %  Another way! :)
%  A = [a,5000,[-1 -2 -3]]
% %% Printing
% fprintf('helloooo...\n')
% disp('world :D')
% disp('A new line without using \n :)')
% %% Cell arrays
% clc
% clear
% a = {6 8 1};
% a{1}
% a{end}              % last element
% a{end+1} = 7;       % add a new element to the cell
% a{:}                % list all the values in one column/row
% b = [a{:}]          % convert the cell to an aray   
% find([a{:}]== 8)    % Does 8 exist in a?
% x = [2 40];           
% y = [6 8 2 9 4];
% ismember(x,y)       % Does x exist in y?
% %% For loops
% for j = 1:length(x) % for loop (for more info look at the help)
%     y(j) = x(j);
% end
% %%************
% %% If condition
% a = 6;
% b = 7;
% if a == b
%     0
% elseif a>=b
%     1
% elseif a~=b & a>b
%     2
% else
%     3
% end
% %% Functions
% [minn, maxx, ave] = mnmxave(8 , 10);
%  hello % Hello world function
% % % %%%*******     
% %% Reading inputs
% % % Creates and opens input dialog box
% answer = inputdlg('Please enter a number:','Pouye says')
% nr = str2num(answer{1})
% result = input('Please enter a number: ')  % Requests user input a number/array/matrix
% result2 = input('What is your name? ','s') % Returns the entered text as a string
% % % % %%************
% %% Sorting..
% sortedX = sort(x);
% % % % % %%************
% %% Timer
% sum=0;
% tic % Start stopwatch timer
% for j=1:(length(x))^3 % for loop (for more info look at the help)
%     sum=sum+1; 
% end
% % toc %Read elapsed time from stopwatch
% t=toc
% %% Plotting
% x = 1:10;
% y = x.*2;
% figure,plot(x,y,'bo')
% hold on,plot(x,y.*2,'r*')
% xlim([-2 12])
% title('Having fun!')
% xlabel('x')
% ylabel('f(x)')
% 
% saveas(gcf,['Having fun.png'])    