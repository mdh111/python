def add(a,b):
    c=a+b
    print("Addition result is ",c)

def subtract(a,b):
    c=a-b
    print("Subtraction result is ",c)

def multiply(a,b):
    c=a*b
    print("Multiplication result is ",c)

def divide(a,b):
    c=a/b
    print("Division result is ",c)

def operation(f,a,b):
    f(a,b)

operation(add,10,20)
operation(subtract,40,20)
operation(divide,50,5)
operation(multiply,3,8)