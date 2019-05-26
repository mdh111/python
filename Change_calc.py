billAmount=int(input("Enter bill amount:"))
paidAmount=int(input("Enter paid amount:"))
balance=paidAmount-billAmount

print("Balance:", balance)

fifty=int(balance/50) 
if fifty>0:
    print("£50:",fifty)
    balance=balance%50

twenty=int(balance/20)
if twenty>0:
    print("£20:",twenty)
    balance=balance%20

ten=int(balance/10)
if ten>0:
    print("£10:",ten)
    balance=balance%10

five=int(balance/5)
if five>0:
    print("£5:",five)
    balance=balance%5

two=int(balance/2)
if two>0:
    print("£2:",two)
    balance=balance%2

if balance>0:
    print("£1:",balance)