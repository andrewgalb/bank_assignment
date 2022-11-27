import uuid


class Account:

    def __init__(self,account_number, account_type, balance):
        if account_number==None:
              self.account_number=uuid.uuid4().hex[:8]
        else:
            self.account_number=account_number  
        self.account_type=account_type
        self.balance=float(balance)

    def deposit(self,amount):
        new_balance=self.balance+float(amount)
        if new_balance<0:
             return False
        else:
             self.balance=new_balance
        return True
    
    def get_balance(self):
        return self.balance

    def __repr__(self):
        return f'{self.account_number}:{self.account_type}:{self.balance}'
