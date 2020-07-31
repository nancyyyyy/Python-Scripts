obj= open("read.txt",'r')
line= obj.read()
for line in obj:
    print(line)
obj.close()
