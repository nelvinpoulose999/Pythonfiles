# Reduce function
from functools import reduce
lst=[2,4,6,8,9]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)
mx=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(mx)


min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)