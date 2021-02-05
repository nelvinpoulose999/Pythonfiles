lst=[1,2,3,4]
num=int(input('enter the number'))
flag=0
value=list()
length=len(lst)
lower=0
upper=len(lst)-1
for i in range(0,length):
    sum=lst[lower]+lst[upper]
    if sum==num:
        print('pairs',lst[lower],lst[upper])
        lower+=1
    elif sum<num:
        lower+=1
    else:
        upper-=1

