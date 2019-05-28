# msg=input("Enter a message:")
# print(msg)

number1=int(input("Enter a number:"))
number2=int(input("Enter a second number:"))
myBoolean=bool(int(input("Enter 1 to add and 0 to multiply:")))

if number1 == 0:
    result=number2
elif number2 == 0:
    result=number1
elif myBoolean==True:
    result=number1+number2
else:
    result=number1*number2

i=1
while i<=10:
    print(result)
    i += 1