# Binary search
arr=[12,50,8,25,60,30,31]
element=int(input('enter the element'))
def search(arr,element):


 flag=0
 arr.sort()
 print(arr)
 length=len(arr)
 print(length)
 lowl=0
 uppl=len(arr)-1
 print(uppl)
 while (lowl<=uppl):
  mid=(lowl+uppl)//2
   #print(arr[mid])
  if(element>arr[mid]):
        lowl=mid+1
  elif(element<arr[mid]):
        uppl=mid-1
  elif(element==arr[mid]):
     return mid
     break
  else:
     return -1
res=search(arr,element)
if(res==-1):
        print('element not found')
else:
        print('element found',arr.index(element))