def convertSingle(single):
    result=""
    mySingle=int(single)
    if mySingle==1:
        result="one"
    elif mySingle==2:
        result="two"
    elif mySingle==3:
        result="three"
    elif mySingle==4:
        result="four"
    elif mySingle==5:
        result="five"
    elif mySingle==6:
        result="six"
    elif mySingle==7:
        result="seven"
    elif mySingle==8:
        result="eight"
    elif mySingle==9:
        result="nine"
    elif mySingle==10:
        result="ten"
    elif mySingle==11:
        result="eleven"
    elif mySingle==12:
        result="twelve"
    elif mySingle==13:
        result="thirteen"
    elif mySingle==14:
        result="fourteen"
    elif mySingle==15:
        result="fiftenn"
    elif mySingle==16:
        result="sixteen"
    elif mySingle==17:
        result="seventeen"
    elif mySingle==18:
        result="eighteen"
    elif mySingle==19:
        result="nineteen"
    return result

def convertDouble(double):
    result=""
    myDouble=int(double)
    if myDouble==10:
        result="ten"
    elif myDouble==20:
        result="twenty"
    elif myDouble==30:
        result="thirty"
    elif myDouble==40:
        result="forty"
    elif myDouble==50:
        result="fifty"
    elif myDouble==60:
        result="sixty"
    elif myDouble==70:
        result="seventy"
    elif myDouble==80:
        result="eighty"
    elif myDouble==90:
        result="ninety"
    return result

def convertNumber(num):
    result = ""
    if num==0:
        result+="zero"
    elif num>=1000 and num<=9999:
        result+=convertSingle(int(num/1000)) + " thousand "
        num%=1000
    if num>=100:
        result+=convertSingle(int(num/100)) + " hundred "
        num%=100
    if num>=20:
        result+=convertDouble(int(num/10)*10)
        num%=10
    if num>0 and num<=19:
        result+=convertSingle(num)
    return result


print(convertNumber(int(input("Enter a number 0-9999:"))))