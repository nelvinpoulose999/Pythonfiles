students={
    1000:{'id':1000,"name":'arun',"course":"django",'qualification':'MCA'},
    1001:{'id':1001,"name":'akhil',"course":"django",'qualification':'Btech'},
    1002:{'id':1002,"name":'gokul',"course":"django",'qualification':'mca'},
    1003:{'id':1003,"name":'amal',"course":"django",'qualification':'Btech'},
    1004:{'id':1004,"name":'nikhil',"course":"django",'qualification':'Btech'}
}
def get_student(**kwargs):

    id=kwargs['id']
    if id in students:
     print(students[id]['name'])
     prop=kwargs['property']
     if prop in students[id]:
         print(students[id][prop])
     else:
        print(students[id]['name'],prop,'property not found')
    else:
        print('invalid id')
#num=int(input('enter the id'))
#get_student(id=num)
get_student(id=1000,property='course')