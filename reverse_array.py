def reverse_array(arr,k):
    n = len(arr)
    k%=n
    reverse(arr, 0 ,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
def reverse(arr,start,end):
    n =len(arr)
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
  
arr = [1, 2, 3, 4, 5, 6]
reverse_array(arr,2)
for num in arr:
        print(num, end=" ")
