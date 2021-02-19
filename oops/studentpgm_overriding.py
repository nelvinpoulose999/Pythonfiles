class Student:
    def __init__(self,rollno,name,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
st=Student(100,'arun','mca',300)
st1=Student(101,'akhil','bca',350)
st2=Student(102,'amal','mca',400)
st3=Student(103,'raj','bca' ,450)
import functools.

functools.reduce
student=[]
student.append(st)
student.append(st1)
student.append(st2)
student.append(st3)
mark=[]
for students in student:
    if students.course=='mca':
        print(students.name)

    mark.append(students.mark)
print(max(mark))