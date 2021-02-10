pattern='ABABC'
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is first recurssive chara")
        break
