class Parent:
    def phone(self):
        print("phone method")

class Child(Parent,):
    pass

ch=Child()
ch.phone()
print(ch)
