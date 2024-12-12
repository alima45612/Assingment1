from random import randint
#allow me to import random integers


def bubbleSort(arr):
    
    n = len(arr)

    
    for i in range(n):
        for y in range(0, n - i - 1):
            
            if arr[y] > arr[y + 1]: #compares the current number with the number next to it, if the number is greater is then swaps it
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                

arr = [randint(-50,100) for i in range(100)] #this generates a list with a range of -50 to 100
print(arr)  # prints the unsorted list
bubbleSort(arr) # calling the function

print("Sorted array is:")

print(arr) #prints the sorted list
