def large(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return(num1)
    elif num2 > num3 and num2 > num1:
        return(num2)
    elif num3 > num1 and num3 > num1:
        return(num3)
    else:
        print("no nu,mber is larger")
num1 = 45
num2 = 65
num3 = 87
print(large(num1, num2, num3))