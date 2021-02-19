class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name + str(self.age)


p=Person('ajay',25)
print(p)
