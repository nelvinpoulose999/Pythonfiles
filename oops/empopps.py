# file is from functional programming

class Employee:
    def __init__(self,id,name,desig,exp,sal):# constructor
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
        return self.name
emplst=[]
f=open("C:/Users/NIKKI/PycharmProjects/myprojects/functional programming/Employee",'r')
for lines in f:
    #print(lines)
    id,name,desig,exp,sal= lines.rstrip('\n').split(',')
    #print(id,name,desig,exp,sal)
    emplst.append(Employee(id,name,desig,exp,sal))
    #print(emplst)
developer=list(filter(lambda emp:emp.desig=='developer',emplst))
for emp in developer:
   print('The developers are:',emp)

# Maximum salary from employees
maxsal=max(list(map(lambda mxsal:mxsal.sal,emplst)))
print('The maximum salary from employees:',maxsal)

# Minimum salary from employees
minsal=min(list(map(lambda mnsal:mnsal.sal,emplst)))
print('The minimum salary from employees:',minsal)
