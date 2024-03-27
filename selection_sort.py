#This sorting technique repeatedly finds the minimum element and sort it in order. Bubble Sort does not occupy any extra memory space. During the execution of this algorithm, two subarrays are maintained, the subarray which is already sorted, and the remaining subarray which is unsorted. During the execution of Selection Sort for every iteration, the minimum element of the unsorted subarray is arranged in the sorted subarray
# Selection Sort algorithm in Python
def selectionSort(array, size):
    
    for s in range(size):
        min_idx = s
        
        for i in range(s + 1, size):
            
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])

# Driver code
data = [ 7, 2, 1, 6 ]
size = len(data)
selectionSort(data, size)

print('Sorted Array in Ascending Order is :')
print(data)
