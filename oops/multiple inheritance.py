class Parent:
    def m1(self):
        print("print")
class Child:
    pass
    # def m2(self):
    #     print('child')
class Subchild(Parent,Child):

    def m3(self):
        print('sub')
su=Subchild()
su.m3()
su.m1()
