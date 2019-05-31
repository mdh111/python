def tax(salary,tax=20):
    incomeTax=salary*tax/100
    print("Your tax is",incomeTax)

tax(1000)

def add(a=10,b=20,c=30):
    result=a+b+c
    print("The result is",result)

add(c=1,a=3)
