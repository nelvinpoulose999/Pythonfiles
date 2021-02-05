lst=[1,2,3,4]
element=int(input('enter the element'))
flag=0
for num in lst:
    for j in lst:
      if((num+j==element) & (num!=j)):
        j += 1
        flag=1

      else:
          flag=0
if flag==1:
    print('the pairs are:', num, j)
else:
    print('no pair found')