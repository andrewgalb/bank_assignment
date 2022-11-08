import uuid

class Account:

    def __init__(self,account_type):
        self.account_number=uuid.uuid4().hex    #(det kan inte finnas flera konton med samma kontonummer)
        self.account_type=account_type
        self.balance=0

    """Returnerar alla transaktioner som en kund har gjort med ett specifikt
    konto eller -1 om kontot inte existerar"""
    def get_all_transactions_by_pnr_acc_nr(self,pnr, acc_nr ):
        raise NotImplementedError