def mergeSort(seq):
    mid = len(seq) // 2
    l1, l2 = seq[:mid], seq[mid:]
    if len(l1) > 1: l1 = mergeSort(l1)
    if len(l2) > 1: l2 = mergeSort(l2)
    tmp = []
    while l1 and l2:
        tmp.append(l1.pop() if l1[-1] > l2[-1] else l2.pop())
    return (l1 or l2) + tmp[::-1]
