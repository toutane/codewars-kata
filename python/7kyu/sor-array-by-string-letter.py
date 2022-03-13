def sort_by_length(arr):
    hadSwap, l = True, len(arr)
    while hadSwap:
        i = 0
        while i < l - 1 and len(arr[i]) <= len(arr[i + 1]):
            i += 1
        if i == l - 1:
            hadSwap = False
        else:
            hadSwap = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print(sort_by_length(["beg", "lif", "i", "to"]))
