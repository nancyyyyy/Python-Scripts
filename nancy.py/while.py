# factorial of 5
# temp is used to secure n from changing its value
n=5
temp=n
fac=1
while n>0:
    fac*=n
    n-=1
n=temp
print('factorial of ',n,'is',fac)