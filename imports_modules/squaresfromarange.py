num = int(input("enter the number"))
lowl = int(input("enter the lower limit"))
uppl = int(input("enter the upper limit"))
def sqr(a,b,c):
 for i in range (1,uppl+1):
    res=i**num
    for j in range(lowl,uppl+1):
        if(j==res):
            print(res)
sqr(num,lowl,uppl)