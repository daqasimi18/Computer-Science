'''
Darab Ali Qasimi
quicksort.py
'''

import unittest
import time

# File name that we want to read its elements and sort
inputFile = "ints-1.dat"

# Split function splits a given array
# The given parameters are inputFile, an array, the lowest index, and the highest index in the array.
def Split(inputFile, array, lindx, hindx):
    # Assign indices for the small elements.
    index = lindx 
    # Last element in the array is chosen as the pivot.
    pivot = hindx
    # Go through elements from the lowest index to the highest
    for i in range(lindx, hindx):
        # If any element is lower than the pivot
        if array[pivot] >= array[i]:
            # Place lower elements in the lower element's index with their values.
            array[i], array[index] = array[index], array[i]
            # Increment the lower element's index.
            index = index+1
    # Place pivot after the values that were lower than the pivot
    # and place the pivot at the index+1.
    array[pivot], array[index] = array[index], array[pivot]
    return (index)

# Quicksort function is the implementation of sorting
# The given parameters are an array, the lowest index, and the highest index.
def Quicksort(array, lindx, hindx):
    # There isn't no need to sort an array that has one element
    if (hindx + lindx) == 1:
        return array
    elif lindx < hindx:
        middle_value = Split(inputFile, array, lindx, hindx)
        # Sort the first half of array from the lowest index upto the middle value or pivot
        Quicksort(array, lindx, middle_value-1)
        # Sort the second half of the array from the middle value to the highest index
        Quicksort(array, middle_value+1, hindx)

# Start timing the algorithm's performace 
start = time.time()
array = []
for i in open(inputFile, "r"):
        # Get rid of the white spaces
        items = i.rstrip()
        # Converting the items to integer in case they are read as strings
        array.append(int(items))
length = len(array)
# The inputFile name is now passed as a parameter to the partition function
Split(inputFile, array, 0, length-1)
# Sort elements of the array from the lowest index upto the last element
Quicksort(array, 0, length-1)
# The given array is sorted now
print(array)

# Stop timing
end = time.time()
# Since the algorithm takes parts of a second 
# therefore rounding off the time to the nearest 4 digits are significant
runn_time = round((end - start), 4)
# Writ the amount of time taken into a new file for record
# the mode of opening the file is "a+" which allows us to create a file and read from the file
store = open('run_time.txt', 'a+')
store.write("%s\r\n" % str(runn_time))

# Testing if the algorithm sorts the arrays as we expect
class TestQuicksort(unittest.TestCase): 
    # This method tests if an unsorted descending array is equal to a sorted ascending array
    def test_sorted(self):
        array1 = [5, 4, 3, 2, 1]
        leng = len(array1)
        # Sort the given array from lowest to highest element in the array
        Quicksort(array1, 0, leng-1)
        # Array is sorted now
        x = array1
        # Check if the sorted array is equal to what we believe is a sorted array
        self.assertEqual(x, [1, 2, 3, 4, 5])
    # This method tests a worst case scenario of the Quicksort algorithm where the array is already sorted
    def test_not_sorted(self):
        # Some float values are passed in the array to check if the algorithm can sort them
        array1 = [1, 2.5, 3, 4.3, 5.2]
        leng = len(array1)
        # Sort the given array from lowest to highest element in the array
        Quicksort(array1, 0, leng-1)
        # Array is sorted now
        x = array1
        # Check if the sorted array is equal to what we believe is a sorted array
        self.assertEqual(x, [1, 2.5, 3, 4.3, 5.2])
if __name__ == '__main__':
    unittest.main() 