import re
rule='KL\d{2}[A-Z]{2}\d{4}'
var_name=input('enter the value')
matcher=re.fullmatch(rule,var_name)# appling patterns to all sting. return match object or one if not match
if matcher==None:
    print('invalid variable name')
else:
    print('valid user name')