import re
#pattern='[abc]'  #here each element in pattern is check in matcher and print as a,b,c.lowercase elements are checked
#pattern='[A-Z]'  #uppercase elements ar checked
#pattern='[a-zA-Z]'#both upper case and lower case elements are checked
#pattern='[0-9]'    # check all digits
#pattern='[a-zA-Z0-9]'#all digits and alphabets are checked
#pattern='[^a-zA-Z0-9]'#^ -used to find all values exept all digits and alphabets are checked


#=================================================================================================
pattern='\s'# check all spaces
pattern='\d'#check all valuse[0-9]
pattern='\D'#[^0-9]
pattern='\w'#[a-zA-Z0-9]
pattern='\W'#special characters
matcher=re.finditer(pattern,'abc _Z7k@')

for match in matcher:
     print(match.start(),match.group())   # returns the position
     #print(match.group())   # returns the object that matches

