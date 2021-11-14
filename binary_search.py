def binary_search(arr,l,r,x):
    re=0
    while l<=r:
        mid=l+(r-1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            l=mid+1
        elif arr[mid]>x:
            r=mid-1
        re=1
            
    if re==0:
        return False
    else:
        return True
    #return False

        


arr=[1,2,3,7,89,44,56,78,43]
x=int(input("enter element to be searched"))
m=binary_search(arr,0,len(arr)-1,x)
if m==False:
    print("element not found")
else:
    print("element found")


