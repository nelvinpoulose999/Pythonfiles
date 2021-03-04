num=int(input('enter the number'))
factorial=1
if num<0:
    print('no should be positive')
elif num==0:
    print('the number is 1')
else:
    for i in range (1,num+1):
        factorial=factorial*i
    print(factorial)

