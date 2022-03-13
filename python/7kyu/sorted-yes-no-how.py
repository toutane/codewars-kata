def is_sorted_and_how(arr):
    i, l = 0, len(arr)
    if arr[0] < arr[1]:
        while i < l - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == l - 1:
            return 'yes, ascending'
    else:
        i = l - 1
        while i > 0 and arr[i] <= arr[i - 1]:
            i -= 1
        if i == 0:
            return 'yes, descending'
    return 'no'


print(is_sorted_and_how([3, 4, 5, 6]))
print(is_sorted_and_how([6, 5, 4, 3]))
