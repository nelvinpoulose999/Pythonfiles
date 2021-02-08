n=int(input('enter the limit'))
for i in range (n,0,-1):
  for j in range(0,n-i):
    print(end=" ")
  for j in range(1,i):
    print('*',end=" ")
  print()
