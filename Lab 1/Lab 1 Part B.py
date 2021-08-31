# Title: Programming Assignment 1 Part B
# Due date: Wednesday, September 1, 2021 at 11:59pm
# Author: Sotheanith Sok
# Description: Implement binary search function

# ------------------------------------------------------------------------------
# imports
import numpy as np

def binary_search_recursive(array, key, start, end):
    # Not found case
    if start > end:
        return -1

    # Searching...
    else:
        # Find mid index
        mid = (start + end) // 2

        # Check if value at mid index is the key
        if array[mid] == key:
            return mid

        # If value at mid smaller than key, search right side...
        elif array[mid] < key:
            return binary_search_recursive(array, key, mid + 1, end)

        # If value at mid index larger than key, search left side...
        else:
            return binary_search_recursive(array, key, start, mid - 1)


done = False

while not done:
    # Get array length
    while True:
        n = input("Enter array length (enter \"done\" to exit): ")
        if n == "done":
            done = True
            break
        elif (n.isnumeric() and int(n) > 0):  # isnnumeric guarantee 0 and positive integers
            n = int(n)  # Convert input to int
            break

    # Check if program should exit
    if done:
        break

    # Generate, sort, and print array
    a = np.random.randint(-10, 11, n)
    a = np.sort(a)
    print("a = %s" % a)

    # Get key
    while True:
        key = input("Enter key (enter \"done\" to exit): ")
        if key == "done":
            done = True
            break
        elif (key.isnumeric() and int(key) > 0):  # isnnumeric guarantee 0 and positive integers
            key = int(key)  # Convert input to int
            break

    # Check if program should exit
    if done:
        break

    # Call binary search algorithm on the array and the key        
    result = binary_search_recursive(a, key, 0, n - 1)

    # Print result
    if result == -1:
        print('Result: Key not found!!!')
    else:
        print('Result: Key found at index %s.' % result)

