def heap_sort(arr):
    def heapify(arr, i, n):
        if i >= (n // 2): return
        largest, left, right = i, 2*i+1, 2*i+2
        if left < n and arr[left] > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest]: largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, largest, n)
    for i in range(len(arr)//2-1, -1, -1):  # build heap in O(n) time
        heapify(arr, i, len(arr))
    for i in range(len(arr), 1, -1):
        arr[i-1], arr[0] = arr[0], arr[i-1]
        heapify(arr, 0, i-1)
