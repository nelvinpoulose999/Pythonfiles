# largest of three numbers
num = int(input("enter 1st number"))
num1 = int(input("enter 2nd number"))
num2 = int(input("enter 3rd number"))
if num > num1:
 print("1st number is larger",num)
elif num > num2:
 print("first number is largest",num)
elif num1 >num2:
    print("2nd number is largest",num1)
elif num==num1==num2:
    print("the numbers are equal")
else:
    print("3rd number is largest",num2)
