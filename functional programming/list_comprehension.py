# square of numbers in a list
lst=[1,2,3,4,5,6]
op=[num**2 for num in lst]
print(op)

# even numbers in a list
even=[num for num in lst if num%2==0]
print(even)

# common elements in  a list
lst1=[1,2,3]
lst2=[3,4,5]
common=[num for num in lst1 if num in lst2]
print(common)
# common1=[num1 for num1 in lst1 for num2 in lst2 if num1==num2]
# print(common1)


# list pair
lst3=[1,2,3]
lst4=[4,5,6]
pair=[(num3,num4) for num3 in lst3 for num4 in lst4 ]
print(pair)

# list in list
lst5=[[10,20],[30,40],[50,60]]
out=[num6 for num5 in lst5 for num6 in num5]
print(out)

# list add and sub
list6=[4,3,2,5,6,7,8]
out1=[num6-1 if num6<5 else num6+1 if num6>5 else 5 for num6 in list6  ]
print(out1)