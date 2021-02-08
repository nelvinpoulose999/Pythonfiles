lst=[1,2,3,4]
element=int(input('enter the element'))
flag=0
sum=0
for num in lst:
    for j in lst:
      sum=num+j
      if((sum==element) & (num!=j)):
        print(num, j)



