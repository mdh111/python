def msg():
    print("hello")
    print("world")

#msg()

def addition(a,b):
    result = a + b
    print("The result is:",result)

#addition(4,8)

def Tax(salary):
    if salary>1500:
        T = salary*0.21
    else:
        T = salary*0.15
    return T

mySalary = int(input("Enter your salary:"))
print("Your tax is",Tax(mySalary))
print("Your net salary is",mySalary-Tax(mySalary))