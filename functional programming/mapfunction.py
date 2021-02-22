#map function
lst=[2,3,4,5,6,7]
square=list(map(lambda num:num**2,lst))
print(square)


name=['akhil','amal','arun']
up=list(map(lambda nam:nam.upper(),name))
print(up)


number=[4,5,8,9,3,2]
val=list(map(lambda num:num-1 if num<5 else num+1,number))
print(val)



