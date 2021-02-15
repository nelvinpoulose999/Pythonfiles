f=open('covid_19_india(1).csv','r')
dict={}
for data in f:
    words=data.rstrip('\n').split(',')
    #1,30/01/20,6:00 PM,Kerala,1,0,0,0,1
    states=words[3].rstrip('***')
    confirmed_cases=words[-1]
    if (states=="Telangana")|(states=="Telengana"):
        states="Telangana"
    if states not in dict:
        dict[states]=int(confirmed_cases)
    else:
        dict[states]=int(confirmed_cases)

for k,v in dict.items():
    print(k,"",v)
print("Highest cases:",max(dict,key=dict.get))
print("Lowest cases:",min(dict,key=dict.get))