import re
rule='KL\d{2}[A-Z]{2}\d{4}'
f=open('vehiclereg','r')
vehlst=[]
for vehnum in f:

    data=vehnum.rstrip('\n')
    matcher=re.fullmatch(rule,data)# appling patterns to all sting. return match object or one if not match

    if matcher==None:
        pass
    else:
        vehlst.append(data)
print(vehlst)


fw=open('outputfil','w')
for out in vehlst:
    fw.write(out+'\n')

