def change(message):
    i=0
    newMessage=""
    while i < len(message):
        if ord(message[i])>=65 and ord(message[i])<=90:
            newMessage += chr(ord(message[i])+32)
        elif ord(message[i])>=97 and ord(message[i])<=122:
            newMessage += chr(ord(message[i])-32)
        elif ord(message[i])>=48 and ord(message[i])<=57:
            newMessage += str(int(message[i])*2)
        else:
            newMessage += message[i]
        i+=1
    return newMessage

print(change(input("Enter a message to convert:")))
