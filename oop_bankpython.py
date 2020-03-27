class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f'Name:\t{self.name}\nBalance:{self.balance}'
    def deposit(self,amt):
        self.balance=self.balance+amt
        print(f'the current balance is:{self.balance}')
    def withdraw(self,amt):
        if self.balance>amt:
            self.balance-=amt
            print('amount withdrawn')
        else:
            print('pls withdraw a lesser amount')
        
