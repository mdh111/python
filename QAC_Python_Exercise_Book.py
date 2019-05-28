# msg=input("Enter a message:")
# print(msg)

number1=int(input("Enter a number:"))
number2=int(input("Enter a second number:"))
myBoolean=bool(int(input("Enter 1 to add and 0 to multiply:")))

if myBoolean==True:
    result=number1+number2
else:
    result=number1*number2

print(result)