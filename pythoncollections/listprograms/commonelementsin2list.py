lst1=[1,2,3,4,50]
lst2=[1,2,3,5,7,8]
pos1=0
pos2=0
cnt=0
while(pos1<len(lst1)) & (pos2<len(lst2)):
#for num in lst1:
   cnt+=1
   if (lst1[pos1]==lst2[pos2]):
       print(lst1[pos1])
       pos1+=1
       pos2+=1

   elif(lst1[pos1]>lst2[pos2]):
       pos2+=1
   else:
       pos1+=1
print(cnt)