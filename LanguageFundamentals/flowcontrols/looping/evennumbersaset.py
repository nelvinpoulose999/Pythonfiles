#print even numbers from a list

limit = int(input("enter the limit"))
lowerl = int(input("enter the lower limit"))
for i in range(lowerl,limit):
    if i%2==0:
        print(i)


