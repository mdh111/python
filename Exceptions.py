try:
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    result=no1/no2
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Only enter digits")
except Exception:
    print("General error")
finally:
    print("Goodbye!")