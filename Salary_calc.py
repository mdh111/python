name=input("Enter name:")
salary=int(input("Enter salary:"))
if salary>2000:
	tax=salary*25/100
else:
	tax=salary*15/100
netSalary=salary-tax
print("Name:",name)
print("Salary:",salary)
print("Net salary:",netSalary)