students={
    1000:{'id':1000,"name":'arun',"course":"django",'qualification':'MCA'},
    1001:{'id':1001,"name":'akhil',"course":"django",'qualification':'Btech'},
    1002:{'id':1002,"name":'gokul',"course":"django",'qualification':'mca'},
    1003:{'id':1003,"name":'amal',"course":"django",'qualification':'Btech'},
    1004:{'id':1004,"name":'nikhil',"course":"django",'qualification':'Btech'}
}
print(students[1004])# print student details of 1004
print(students[1004]['qualification'])# print the qualification of 1004

id=int(input(('enter the students id')))
#property=input('enter student property')
if id in students:
    property = input('enter student property')
    if property in students[id]:
     print(students[id]['name'],students[id][property])
    else:
     print(students[id]['name'],property,'no found')
else:
    print('id not found')
