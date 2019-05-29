listLength = int(input("How long do you want your list to be?"))

myList=[]
i=1
while i <= listLength:
    myList.append(i)
    i+=1
print(myList)

newList=[]
for each in myList:
    newList.append(each*10)
print(newList)

