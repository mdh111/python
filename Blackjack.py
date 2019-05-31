def blackjack(a,b):
    if a>21 and b>21:
        return 0
    elif a>b and a<=21:
        return a
    elif b>a and b<=21:
        return b
    else:
        return a

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(blackjack(num1,num2))