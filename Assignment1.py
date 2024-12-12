from random import randint


def bubbleSort(arr):
    
    n = len(arr)

    
    for i in range(n):
        for y in range(0, n - i - 1):
            
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                

arr = [randint(-50,100) for i in range(100)]
print(arr)
bubbleSort(arr)

print("Sorted array is:")

print(arr)
