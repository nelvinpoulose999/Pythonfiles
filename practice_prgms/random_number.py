import random
n=random.randint(0,100)
print(n)
count=0
while n!='guess':
    if count==5:
        print('Ypu lost the game')
        break
    guess=int(input('enter the number'))
    if guess>n:
        print("the number is greater")
    elif guess<5:
        print('the number is small')
    else:
        print("you won the game")
        break

    count+=1