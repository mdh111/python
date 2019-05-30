alphaList=[0]*26
message=input("Enter a message:")
message=message.upper()
i=0
while i<len(message):
    if ord(message[i])>=65 and ord(message[i])<=90:
        alphaList[ord(message[i])-65]+=1
    i+=1
i=0
while i<=25:
    if alphaList[i]>0:
        print(chr(i+65),"=",alphaList[i])
    i+=1
