def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i
        while j > 0 and tmp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = tmp
    return arr
