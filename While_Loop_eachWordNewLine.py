msg=input("Enter your message:")
i=0
word=""
while i<len(msg):
    if msg[i]!=" ":
        word += msg[i]
    else:
        print(word)
        word=""
    i += 1
print(word)