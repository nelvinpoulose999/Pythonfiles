f=open('moviedetails.csv','r')
dict={}
for movies in f:
    data=movies.rstrip('\n').split(' ')
    #print(data)
    #"imdbId","title","releaseYear","releaseDate","genre","writers","actors","directors","sequel","hitFlop"
    films=data[1]
    year=data[2]
    #print(films,year)
    if year not in dict:
        dict[year]=films
    else:
        pass
#print(dict)
for k,v in dict.items():
    print(k,' ',v)