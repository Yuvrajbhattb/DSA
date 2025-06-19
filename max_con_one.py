def max_con_one(arr):
    n = len(arr)
    count = 1
    maxcount = 0
    i=1
    for i in range(n-1):
        if  arr[i-1]==arr[i]:
            count+=1
        else:
            maxcount = max(maxcount,count)
            count=1
    return max(maxcount,count)
    
    
arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print(max_con_one(arr))
