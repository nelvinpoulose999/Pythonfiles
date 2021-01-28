num =int(input("enter the number"))
result=" "
while num!=0:
    digit=num%10
    print(digit)
    digit^3
    print(digit)
    result+=str(digit)
    num=num//10
print(result)
