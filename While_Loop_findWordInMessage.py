msg=input("Enter your message:")
what=input("What are you looking for?")
i=0
count=0
while i<len(msg):
    if msg[i] == what[0]:    
        if (msg[i:len(what)+i]) == what:
            count += 1
            i = i + len(what)-1
    i += 1
print(count)