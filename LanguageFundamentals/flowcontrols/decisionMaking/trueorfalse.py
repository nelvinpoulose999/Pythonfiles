# print true if num+num1==100,num1==100,num==100
num = int(input("enter 1st number"))
num1 = int(input("enter 2nd number"))
sum=num+num1
if (sum==100)|(num==100)|(num1==100):
    print("the number is true")
else:
    print("the number is false")
print(sum)