class Personaldetails:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("name:", self.name)
        print("Age:",self.age)
        print("place:",self.place)
        print("year:",Personaldetails.year)

obj=Personaldetails("Akhil",20,"ernakulam")
obj.display()
print("----------------------------------------------------------")
Personaldetails.year=Personaldetails.year+1
obj.add_age()
obj.relocate("thrissur")
obj.display()
print('---------------------------------------')
Personaldetails.year=Personaldetails.year+1
obj.add_age()
obj.relocate("delhi")
obj.display()