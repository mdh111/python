ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirtenn","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

num=int(input("Enter a number 0-9999:"))


result = ""
if num==0:
    result+="zero"
elif num>=1000 and num<=9999:
    result+=ones[int(num/1000)] + " thousand "
    num%=1000
if num>=100:
    result+=ones[int(num/100)] + " hundred "
    num%=100
if num>=20:
    result+=tens[int(num/10)] + " "
    num%=10
if num>0 and num<=19:
    result+=ones[num]
print(result)