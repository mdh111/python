count=5
while count!=0:
    print(count)
    count-=1    #augmented assignment shorthand

while True:
    response = input()
    if int(response) % 5 == 0:
        print("Number is divisable by 5!")
        break
        