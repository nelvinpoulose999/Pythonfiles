icc_test_wc_table={
    'England':{'id':'England','pct':70.2,'point':442,'series':6,'won':11,'lost':4,'drawn':3},
    'New Zeland':{'id':'New Zeland','pct':70.0,'point':420,'series':5,'won':7,'lost':4,'drawn':0},
    'Australia':{'id':'Australia','pct':69.2,'point':332,'series':4,'won':8,'lost':4,'drawn':2},
    'India':{'id':'India','pct':68.3,'point':430,'series':6,'won':9,'lost':4,'drawn':1},
    'Pakistan':{'id':'Pakistan','pct':43.3,'point':286,'series':5.5,'won':4,'lost':5,'drawn':3},
    'West indies':{'id':'West indies','pct':33.3,'point':160,'series':4,'won':3,'lost':6,'drawn':0},
    'South Africa':{'id':'South Africa','pct':30.0,'point':144,'series':4,'won':3,'lost':8,'drawn':0},
    'Srilanka':{'id':'Srilanka','pct':16.7,'point':80,'series':4,'won':1,'lost':6,'drawn':1},
    'Bangladesh':{'id':'Bangladesh','pct':0.0,'point':0,'series':2.5,'won':0,'lost':6,'drawn':0}
}

# Points of teams more than 300
for data_of_wc in icc_test_wc_table:
    pts=icc_test_wc_table[data_of_wc]['point']
    if pts>=300:
        print(icc_test_wc_table[data_of_wc]['id'],' - ',pts)

# Matches won more than 5
for matchwin in icc_test_wc_table:
    matchwon=icc_test_wc_table[matchwin]['won']
    if matchwon>=5:
        print(icc_test_wc_table[matchwin]['id'],' - ',matchwon)

# print percentage of teams
percentage=float(input('enter the percentage'))
for percent in icc_test_wc_table:
    pctpoints=icc_test_wc_table[percent]['pct']
    if percentage<=pctpoints:
        print(icc_test_wc_table[percent]['id'],' - ',pctpoints)
    # else:
    #     pass
    # break

# print the property that as input
id = input('enter the id')
if id in icc_test_wc_table:
        property = int(input("enter the property"))
        if property in icc_test_wc_table[id]:
            print(icc_test_wc_table[id]['id'],icc_test_wc_table[id][property])
        else:
            print(icc_test_wc_table['id'], property,'not found')
else:
    print('id not found')