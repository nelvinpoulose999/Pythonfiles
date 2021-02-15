def add(num1,num2):
    return num1+num2


def add(num1,num2,num3):
    return num1+num2+num3 # recently added function only works
# if print(add(20,30)) doesn't work boz recent function has 3 numbers


#add(10,20,30)
print(add(10,20,30))

# *can be used to call/passed any number values from function
def add(*num):  #* tuple format
    print(max(num))
    print(sum(num))
    print(num)
add(10,20,30,40,50,60) # taken in the form of tuple


def print_employee(**args): # ** dictionary format
    print(args)
print_employee(id=100,name='ajay',jlocation='kakkanad',home='thrissur') # taken as dictionary