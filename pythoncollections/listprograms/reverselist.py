arr=[12,50,8,25,60,30,31]
element=int(input('enter the element'))
arr.sort()
arr.reverse()
print(arr)
flag=0
lowl=0
uppl=len(arr)-1
print(uppl)
while (lowl<=uppl):
    mid=(lowl+uppl)//2
    if(element<arr[mid]):
        lowl=mid+1
    elif(element>arr[mid]):
        uppl=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if(flag==1):
    print('element found',arr.index(element))
else:
    print('element not found')