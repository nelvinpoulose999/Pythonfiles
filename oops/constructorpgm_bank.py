class Bank:
    bankname='SBK'  # class variable/static variable it is used for reduce memory allocations
    def __init__(self,accno,pname,minbalance):# creating constructor
        self.accno=accno         #}
        self.personname=pname    #} instance variable(self.accno,self.personname,etc
        self.balance=minbalance  #}
        print(' Account number:',self.accno,'\n','Account holder:',self.personname,'\n','Account balance:',self.balance,'\n','Name of bank:',Bank.bankname)

    def deposit(self,amount):
        self.balance+=amount
        print( self.personname,'account credited with:',amount,'\n','balance amount:',self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(' account debited with:', amount,'\n','balance amount:', self.balance)
password=(1234)
pswrd=int(input("enter the password"))
if pswrd==password:

    accno=int(input("enter thre account number"))
    name=input("enter the name")
    balance=3000

    obj = Bank(accno,name,balance)
    dep= int(input('enter the amount'))

    obj.deposit(dep)
    obj.withdraw(2000)

else:
    print("invalid pswrd")