msg=input("Enter a message:")
msg=msg+" "
myList=[]
word=""
newMsg=""
exists=False
for each in msg:
    if each!=" ":
        word+=each
    else:
        for eachWord in myList:
            if word == eachWord:
                exists = True
        if exists != True:
            newMsg+=word + " "
        myList.append(word)
        word=""
        exists = False
print(newMsg)