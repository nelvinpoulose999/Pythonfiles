str='ABABC'
len=len(str)
res=0
for i in range (0,len):
    for j in range (i+1,len):
        if(str[i]==str[j]):
            print(str[i])
    break
