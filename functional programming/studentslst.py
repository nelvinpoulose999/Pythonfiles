class Student:
    def __init__(self,rollno,name,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def __str__(self):
        return self.name
st=Student(100,'arun','mca',300)
st1=Student(101,'akhil','bca',350)
st2=Student(102,'amal','mca',400)
st3=Student(103,'raj','bca' ,450)

student=[st,st1,st2,st3]

#   Map function only
#   upper case to all students name
upst=list(map(lambda stud:stud.name.upper(),student))
print(upst)

#   adding 50 marks to their matrk
bmark=list(map(lambda bonus:bonus.mark+50,student))
print(bmark)

#  USING MAP AND FILTER FUNCTION - ONLT STUDENTS WITH MCA

courses=list(map(lambda st:st.name,list(filter(lambda cours:cours.course=='mca',student))))
print(courses)


# maximum & minimum mark in students


mxmark=max(list(map(lambda maxv:maxv.mark,student)))
print(mxmark)
mnmark=min(list(map(lambda minv:minv.mark,student)))
print(mnmark)

