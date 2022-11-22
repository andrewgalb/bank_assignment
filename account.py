import uuid


class Account:

    def __init__(self,account_number, account_type, balance):
        if account_number==None:
              self.id=uuid.uuid4().hex[:8]
        else:
            self.account_number=account_number  
        self.account_type=account_type
        self.balance=float(balance)

    """Returnerar alla transaktioner som en kund har gjort med ett specifikt
    konto eller -1 om kontot inte existerar"""
    def get_all_transactions_by_pnr_acc_nr(self,pnr, acc_nr ):
        raise NotImplementedError

    def deposit(self,amount):
        self.balance+=float(amount)
        return True
    
    def get_balance(self):
        return self.balance

    def __repr__(self):
        return f'{self.account_number}:{self.account_type}:{self.balance}'
