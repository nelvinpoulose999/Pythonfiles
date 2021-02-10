pattern='ABABCD'
dit={}
for ch in pattern:
    if ch not in dit:
        dit[ch]=1
    else:
        dit[ch]+=1
print(dit)
print(min(dit,key=dit.get))

for k,v in dit.items():
    if v==1:
        print(k)
        break