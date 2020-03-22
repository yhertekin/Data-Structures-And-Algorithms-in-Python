def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubbleSort(test)
print(test)