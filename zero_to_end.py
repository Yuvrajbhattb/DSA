def zero_to_end(arr):
   n = len(arr)
   count = 0
   for i in range(n):
       if(arr[i]!=0):
           arr[count]=arr[i]
           count+=1
   while (count<len(arr)):
           arr[count]=0
           count+=1
       
arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
zero_to_end(arr)
for num in arr:
        print(num, end=" ")
