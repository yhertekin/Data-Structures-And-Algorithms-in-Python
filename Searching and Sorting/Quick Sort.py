def part(arr, start, end):
    pivot = arr[start]
    low = start+1
    high = end
    
    while True:
        while low <= high and arr[high] >= pivot:
            high-=1
        
        while low <= high and arr[low] <= pivot:
            low+=1
    
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    return high
    

def quicksort(arr, start, end):
    
    if start >= end:
        return
    
    p = part(arr, start, end)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)
    return arr
   
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, len(test)-1)