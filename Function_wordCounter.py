def wordCount(message):
    i=0
    words=1
    while i < len(message):
        if message[i]==" ":
            words+=1
        i+=1
    return words

myMessage=input("Enter a mesage:")
print("There are",wordCount(myMessage),"words")


