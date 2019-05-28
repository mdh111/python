msg=input("Enter a message:")
char=input("Which letter are you looking for?")
count=0
i=0
while i < len(msg):
    if msg[i] == char:
        count = count + 1
    i = i + 1
print("The character",char,"appears",count,"times")
    

    
