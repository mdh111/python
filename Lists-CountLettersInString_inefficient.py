def countalpha(message,alpha):
    i=0
    count=0
    message=message.upper()
    while i<len(message):
        if message[i] == alpha:
            count+=1
        i+=1
    if count>0:
        print(alpha,"=",count)
    return count

msg=input("Enter a message:")
i=65
counter=len(msg)
while i<=90 and counter>0:
    counter = counter + countalpha(msg,chr(i))
    i+=1


