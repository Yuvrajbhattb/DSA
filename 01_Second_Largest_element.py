def second_largest(arr):
    first = -1
    second  = -1
    for i in range(len(arr)):
        if arr[i]>first:
            second = first
            first = arr[i]
        elif arr[i]>second:
            second = arr[i]
    return second

arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr))
