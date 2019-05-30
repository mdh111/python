fileRead=open("data.txt","r")
fileWrite=open("data2.txt","w")
for each in fileRead:
    for c in each:
        if c=="a":
            print("*",file=fileWrite,end="")
        else:
            print(c,file=fileWrite,end="")