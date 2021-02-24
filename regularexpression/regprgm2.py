import re
# pattern='a+'# consiqutive a's
# pattern='a*'# any number of a including position without values
pattern='a{2}'# groups as 2 number of a
pattern='a{2,3}'# min 2 a and max 3 a
matcher=re.finditer(pattern,'aaaaaabcaaaacaaaaa _Z7k@')

for match in matcher:
     print(match.start(),match.group())   # returns the position
     #print(match.group())   # returns the object that matches
