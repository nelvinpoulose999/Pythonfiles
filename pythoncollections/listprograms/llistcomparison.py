list1=[1,2,3,4,50]
list2=[1,2,5,7,8,3]
result=[]
# def list_common(list1,list2):
#  result=[]
#  for x in list1:
#     if x in list2:
#         result.append(x)
#     return result
#     break
#  else:
#      return -1
# res=list_common(list1,list2)
# if(res==-1):
#  print('no result')
# else:
#     print(res)
for x in list1:
    if x in list2:
        result.append(x)
print('the common elements are:',result)

