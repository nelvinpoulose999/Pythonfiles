text='hello hai hello how hai'
print(text)
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)

max=0
fkey=" "
for i in dict:
    print(i)
    element=i
    key=dict[i]
    print(key)
    if key>max:
        max=key
        fkey=element
print(max,fkey)
