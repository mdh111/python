def addition(a,b):
    c=a+b
    print("Addition result is ",c)

def subtraction(a,b):
    c=a-b
    print("Subtraction result is ",c)

def operation(f,a,b):
    f(a,b)

operation(addition,10,20)
operation(subtraction,40,20)