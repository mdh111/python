
def reverseWord(msg):
    i=len(msg)-1
    new=""
    while i >=0:
        new+=msg[i]
        i-=1
    return new

msg=input("Enter your message:")
i=0
word=""
newMsg=""
while i<len(msg):
    if msg[i]!=" ":
        word += msg[i]
    else:
        newMsg = newMsg + " " + reverseWord(word)
        word=""
    i += 1
print(newMsg + " " + reverseWord(word))
