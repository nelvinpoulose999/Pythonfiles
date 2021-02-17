# oops(object oriented programming)
class Person:
    def set_values(self,name,age):
         self.age=age
         self.name=name
    def print_value(self):
        print(self.name)
        print(self.age)

obj = Person()
obj.set_values(25,'Amal')
obj.print_value()

obj1=Person()
obj1.set_values(30,'Arun')
obj1.print_value()
