f=open("demofile","r") #path of file or file name ,operation
lst=[]
name=set()
for lines in f:
    lst.append(lines.rstrip('\n')) #.rstrip used to strip the unwanted elements
    name.add(lines.rstrip('\n'))
print(lst)
print(name)
