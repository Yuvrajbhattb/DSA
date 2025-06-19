def second_largest(arr):
    n = len(arr)
    arr.sort()
    maxnum = max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])   
    return maxnum
arr = [10, 3, 5, 6, 20]
print(second_largest(arr))
