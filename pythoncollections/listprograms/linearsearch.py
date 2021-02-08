arr=[10,11,12,13,14,15,16,18]
element=int(input('enter the element'))
res=0
for num in arr:
    if element==num:
        res=1
        break
       #res+=1
if res==1:
    print("element found")
else:
    print("element not found")
