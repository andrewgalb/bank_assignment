import uuid


class Account:

   

    def __init__(self,account_type):
        self.account_number=uuid.uuid4().hex[:8]   #(det kan inte finnas flera konton med samma kontonummer)
        self.account_type=account_type
        self.balance=0

    def __init__(self,account_number, account_type, balance):
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance

    """Returnerar alla transaktioner som en kund har gjort med ett specifikt
    konto eller -1 om kontot inte existerar"""
    def get_all_transactions_by_pnr_acc_nr(self,pnr, acc_nr ):
        raise NotImplementedError

    def deposit(self,amount):
        self.balance+=amount
        return True
    
    def get_balance(self):
        return self.balance

    def __repr__(self):
        return f'{self.account_number} {self.account_type} {self.balance}'
