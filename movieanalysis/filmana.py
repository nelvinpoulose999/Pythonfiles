f=open('movies.csv','r')
dict={}
for filmdata in f:
   movie=filmdata.rstrip('\n').split(' ')
   year=movie[2]

   if year not in dict:
       dict[year]=1
   else:
       dict[year]+=1
print(dict)