product=input("Product name: ")
price=input("Product price: ")
qty=input("Product quantity: ")
amount=float(price)*int(qty)
vat=amount*15/100
bill=amount+vat
print("Your Bill")
print("Product: ",product)
print("Amount: ",amount)
print("VAT: ",vat)
print("Total bill: ",bill)