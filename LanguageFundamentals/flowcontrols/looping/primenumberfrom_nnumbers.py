# prime numbers from 1-num
num=int(input("enter the limit"))
for i in range(1,num+2):# i=1,2
    flag=0
    for j in range (2,i):# (2,1),(2,2)
         if(i%j==0):# 1%2==0-not equal,2%2==0,3%2==0-not equal
             flag=1
             break
         else:
             pass
    if(flag==0):
         print("the number is prime number", i)
    else:
          print("the number is not prime number")
