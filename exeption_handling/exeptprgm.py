num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
try: #doubtful code is execuited here
    res=num1/num2
    print(res)
except Exception as e: #Exeption is ain built class and e is given as aliasing value
    print(e.args,'\n','Exeption completed')
print('database operation')
print('file execuited')
