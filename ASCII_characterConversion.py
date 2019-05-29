a = input("Enter any character:")
b = ord(a)    
if b>=65 and b<=90:
    print("Upper case")
elif b>=97 and b<=122:
    print("Lower case")
elif b>=48 and b<=57:
    print("Number")
else:
    print("Any other character")
