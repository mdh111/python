""" numbers=[1,34,3,23,26]
i=0
while i<5:
    print(numbers[i])
    i+=1 """

numbers=[]
while True:
    num=int(input("Enter a number:"))
    if num==0:
        break
    else:
        numbers.append(num)

highest=numbers[0]
i=1
while i < len(numbers):
    if numbers[i]>highest:
        highest=numbers[i]
    i+=1
print("Highest numbers is ",highest)

print(numbers)
