lst=[4,3,5]
tot=0
res=list()
tot=sum(lst)
for num in lst:
    #sum=sum+num
    #res=tot-num
    res.append(tot - num)
print(res)
#find using 2 for loop