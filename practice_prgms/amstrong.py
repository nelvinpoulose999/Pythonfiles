# amstrong number
def amst():
    num=int(input("enter the number"))
    value=num
    sum=0
    for i in range(0,num):
        digit=num%10
        sum=digit**3+sum
        num=num//10
    if value==sum:
        print(value,'the number is amstrong')
    else:
        print(value,'not a amstrong')
amst()