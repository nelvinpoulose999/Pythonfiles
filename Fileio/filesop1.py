f=open('news','r')
name=set()
for line in f:
    words=line.rstrip('\n').split(' ')

    for word in words:
        name.add(word)
print(name)
for word in name:
    print(word)