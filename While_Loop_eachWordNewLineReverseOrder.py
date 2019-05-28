msg=input("Enter your message:")
i=len(msg)-1
word=""
while i>=0:
    if msg[i]!=" ":
        word = msg[i] + word
    else:
        print(word)
        word=""
    i -= 1
print(word)