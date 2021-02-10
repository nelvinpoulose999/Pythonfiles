population= {'ind':100,'china':200,'nz':10,'wi':20,'aus':30}
population.get('ind')
print(population)
print(population['ind'])
data= sorted(population)#sorted based on keys
data=sorted(population,key=population.get,reverse=True)# get is used to access the values of the key,reverse is used to reverse the order
print(data)