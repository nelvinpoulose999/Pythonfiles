#prime number 1 & that number
limit = int(input("enter the limit"))
flag=0
for i in range (2,limit):
    if(limit%i==0):
        flag=1
        break
    else:
        pass
if(flag==0):
    print("prime number")
else:
    print("not a prime")