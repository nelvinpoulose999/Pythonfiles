lst = [3,4,6,7,8]
elist=list()
olist=[]
for even in lst:
    if(even%2==0):
        elist.append(even)

    else:
        olist.append(even)
print(elist)
print(olist)
