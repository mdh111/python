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
    elif mySingle==0:
        result="zero"
    return result

def convertDouble(double):
    result=""
    myDouble=int(double)
    if myDouble==1:
        result="ten"
    elif myDouble==2:
        result="twenty"
    elif myDouble==3:
        result="thirty"
    elif myDouble==4:
        result="forty"
    elif myDouble==5:
        result="fifty"
    elif myDouble==6:
        result="sixty"
    elif myDouble==7:
        result="seventy"
    elif myDouble==8:
        result="eighty"
    elif myDouble==9:
        result="ninety"
    return result

def convertOneDigitNumber(num):
    myNum = str(num)
    result = ""
    result += convertSingle(int(myNum))
    return result

def convertTwoDigitNumber(num):
    myNum = str(num)
    result = ""
    result += convertDouble(int(myNum[0]))
    result += " "
    if int(myNum[1])>0:
        result += convertSingle(int(myNum[1]))
    return result

def convertThreeDigitNumber(num):
    myNum = str(num)
    result = ""
    result += convertSingle(int(myNum[0]))
    result += " hundred "
    result += convertTwoDigitNumber(int(myNum[1:3]))
    return result

def convertFourDigitNumber(num):
    myNum = str(num)
    result = ""
    result += convertSingle(int(myNum[0]))
    result += " thousand "
    result += convertThreeDigitNumber(int(myNum[1:4]))
    return result

def convertNumber(num):
    myNum = str(num)
    result = ""
    if len(myNum)==1:
        result += convertOneDigitNumber(num)
    elif len(myNum)==2:
        result += convertTwoDigitNumber(num)
    elif len(myNum)==3:
        result += convertThreeDigitNumber(num)
    elif len(myNum)==4:
        result += convertFourDigitNumber(num)
    else:
        result += "Number out of range"
    return result

print(convertNumber(int(input("Enter a number 0-9999:"))))