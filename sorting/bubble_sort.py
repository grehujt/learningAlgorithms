def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        swapped = False
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: break
    return arr
