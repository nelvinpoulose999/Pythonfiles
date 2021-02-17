class Bank:
    bankname='SBK'  # class variable/static variable it is used for reduce memory allocations
    def create_account(self,accno,pname,minbalance):
        self.accno=accno         #}
        self.personname=pname    #} instance variable(self.accno,self.personname,etc
        self.balance=minbalance  #}
        print(self.accno,self.personname,self.balance,Bank.bankname)

    def deposit(self,amount):
        self.balance+=amount
        print(self.personname,'account credited with',amount,'the balance amount',self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print('account debited with', amount, 'the balance amount', self.balance)

obj = Bank()
obj.create_account(1000,'Akhil',3000)
obj.deposit(5000)
obj.withdraw(2000)


