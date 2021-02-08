sum=0
expe=[]
employee=[
    [100,'akhil','developer',2,'50000',1989,1995],
    [101,'anu','developer',2,'50000',1970,1990],
    [102,'anand','qa',1,'30000',1989,1991],
    [103,'james','ba',1,'40000',1998,1999]
]
#print employees worked in 1990's
#print exper of each empoyee
#high exp employee details




for emp in employee:
    print(emp[1])# employee name

for emp in employee:# emp salary
    print(emp[4])

for emp in employee:#dev details
    if(emp[2]=='developer'):
        print(emp)

for emp in employee:
    str=int(emp[4])
    sum=sum+str
print(sum)

sallist=[]
for emp in employee:
 sallist.append(emp[4])
print(max(sallist))

for emp in employee:
    if (emp[6]>1990):
        print(emp)

for emp in employee:
    exp=emp[6]-emp[5]
    print(emp[1],exp,'years')

for emp in employee:
    exp = emp[6] - emp[5]
    expe.append(exp)
print('the max experience:',max(expe))
high=max(expe)
for emp in employee:
 exp = emp[6] - emp[5]
 if (high==exp):
     print(emp)
