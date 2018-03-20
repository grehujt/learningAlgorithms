def quick_sort(arr):
    if len(arr) < 2: return arr
    p, seq = arr[0], arr[1:]
    return quick_sort([x for x in seq if x <= p]) + [p] + quick_sort([x for x in seq if x > p])
