list1=[1,2,3,5,50]
list2=[1,3,9,15,40]
result=[]
for i in list1:
    for j in list2:
        if(i==j):
            result.append(i)
        elif(i>j):
            j+=1
        elif(i<j):
            i+=1
print(result)