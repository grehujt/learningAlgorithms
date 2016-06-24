def quickSort(arr):
    def partition(arr):
        p, seq = arr[0], arr[1:]
        return [x for x in seq if x<=p], p, [x for x in seq if x>p]
    if len(arr) <= 1: return arr
    lo, p, hi = partition(arr)
    return quickSort(lo) + [p] + quickSort(hi)
