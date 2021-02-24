#regular expression
import re
pattern='ab'# print as ab
matcher=re.finditer(pattern,'ababaaabbbbabab')
count=0
for match in matcher:
     print(match.start())   # returns the position
     print(match.group())   # returns the object that matches
     count+=1
print('the no of counts',count)


