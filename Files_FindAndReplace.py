fileRead=open("data.txt","r")
fileWrite=open("data2.txt","w")
old=input("What would you like to replace?")
new=input("What would you like to replace that with?")
for each in fileRead:
    i=0
    while i<len(each):
        if each[i]==old[0]:
            if(each[i:len(old)+i]) == old:
                print(new,file=fileWrite,end="")
                i+=len(old)
            else:
               print(each[i],file=fileWrite,end="")
               i+=1 
        else:
            print(each[i],file=fileWrite,end="")
            i+=1
