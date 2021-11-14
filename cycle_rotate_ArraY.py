arr=[1,2,3,4,5]
n=len(arr)
x=arr[n-1]
i=n-1

while i!=-1:
    print(i,i-1)
    i+=1
    #arr[i]=arr[i-1]
arr[-1]=x
print(arr)
