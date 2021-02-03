lst=[4,3,5]#8,9,7
num1=[5,6,7]# 13,12,11
res1=[]
tot=0
tot1=0
res=list()
tot=sum(lst)
for num in lst:
#sum=sum+num
#res=tot-num
 res.append(tot - num)
print(res)


# find using 2 for loop
for num2 in num1:
   tot1=tot1+num2
for num2 in num1:
     res1.append(tot1-num2)
print(res1)