# secondlargest
num = int(input("enter 1st number"))# 5
num1 = int(input("enter 2nd number"))#4
num2 = int(input("enter 3rd number"))#3
if (num>num1) & (num>num2):#5>4,5>3
    if num1>num2:
     print("2nd number is second larger",num1)
    else:
     print(("3rd is second larger",num2))
elif (num1>num)&(num1>num2):
    if num>num2:
        print("1st is second largest",num)
    else:
        print("3rd is second largest",num2)
elif (num2>num)&(num2>num1):
    if(num>num1):
        print("1st number is second largest",num)
    else:
        print("2nd number is second largest",num1)


