fileRead=open("data.txt","r")
fileWrite=open("data2.txt","w")
for each in fileRead:
    print(each,file=fileWrite,end="")

print("hello",end=" ")
print("world")