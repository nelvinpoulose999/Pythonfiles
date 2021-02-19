class Parent:
    def m1(self):
        print('print parent')
class Child(Parent):
    def m2(self):
        print('child')
class Subchild(Child):
    def m3(self):
        print('subchild')
su=Subchild()
su.m3()
su.m2()
su.m1()

ch=Child()
ch.m1()
ch.m2()


pa=Parent()
pa.m1()
