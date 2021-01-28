num=int(input("enter a number"))
result=" "
while num!=0:
    digit=num%10
    result+=str(digit)
    num=num//10
print(result)




