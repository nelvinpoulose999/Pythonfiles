student={'roll no.':100,'name':'akhil','course':'MCA'}
print(student)
if 'total' in student:
    print('key found')
else:
    student['total']=150
print(student)
student['total']+=50
print(student)
