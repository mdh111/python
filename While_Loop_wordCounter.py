msg=input("Enter a message:")
i=0
words=0
while i < len(msg):
    if msg[i]==" ":
        words = words+1
    i=i+1
print("There are",(words+1),"words")
