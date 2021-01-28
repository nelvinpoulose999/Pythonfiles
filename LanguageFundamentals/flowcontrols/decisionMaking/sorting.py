# sorting in any order
#num = [10,20,5,25,22,2]
#num.sort()
#print(num)
#num.sort(reverse=True)
#print(num)
num = int(input("enter 1st number"))
num1 = int(input("enter 2nd number"))
num2 = int(input("enter 3rd number"))
#if num>num1:
#    temp=num
#    num=num1
#    num1=temp
#elif num1>num2:
#       temp1=num1
#       num1=num2
#       num2=temp1

#elif num2>num:
#        temp2=num2
 #       num2=num
#        num=temp2
#elif num<num1:
#    temp3 = num
#    num = num1
#    num1 = temp3
#elif num1<num2:
#    temp4 = num1
#    num1 = num2
#    num2 = temp4
#elif num2<num:
 #   temp5 = num2
 #   num2 = num
 #   num = temp5
if (num>num1)&(num>num2):
    if(num1>num2):
print(num,num1,num2)