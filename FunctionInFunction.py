def operation(day):
    if day == 1:
        def fun(A,B):
            C=A+B
            print("Addition result is ",C)
    if day == 2:
        def fun(A,B):
            C=A-B
            print("Subtraction result is ",C)
    return fun

today=operation(2)
today(2,5)