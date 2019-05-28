msg=input("Enter your message:")
what=input("What are you looking for?")
i=0
count=0
while i<len(msg):
    if (msg[i:len(what)+i]) == what:
        count = count + 1
    i += 1
print(count)