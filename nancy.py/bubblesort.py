a=[2,7,3,9,5,6]
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j-1]>a[j]:
             a[j-1],a[j]=a[j],a[j-1]


       

print(a)
