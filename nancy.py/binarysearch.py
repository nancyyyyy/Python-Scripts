a=[3,4,6,8,9]
def binary_tree(a,key,start,end):
    if start<=end:
        mid=int((start+end)/2)
        if a[mid]>key:
            return binary_tree(a,key,start,mid-1)
        elif a[mid]<key:
            return binary_tree(a,key,mid+1,end)
        else:
            return mid
            # nancysom
            # nancy
            #som
    print(key,"key could not found")
    return -1
print(binary_tree(a,4,0,len(a)-1))
    
    