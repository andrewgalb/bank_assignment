import uuid
from transaction import Transaction
from account import Account

class Customer:

    accounts=[]
    transactions=[]

    def __init__(self,name,ssn):
        self.id=uuid.uuid4().hex
        self.name=name
        self.ssn=ssn

    def __init__(self,id, name,ssn):
        self.id=id
        self.name=name
        self.ssn=ssn     

    def __repr__(self):
        return f'{self.id} {self.name} {self.ssn}'

    """Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret som
    det skapade kontot fick alternativt returneras –1 om inget konto skapades."""
    def add_account(self,pnr):
        raise NotImplementedError

    """Returnerar Textuell presentation av kontot med kontonummer som tillhör
    #kunden (kontonummer, saldo, kontotyp)."""
    def get_account(self,pnr, account_id):
        raise NotImplementedError

    """Gör en insättning på kontot, returnerar True om det gick bra annars False."""
    def deposit(self,pnr, account_id, amount):
        raise NotImplementedError

    """Gör ett uttag på kontot, returnerar True om det gick bra annars False."""
    def withdraw(self,pnr, account_id, amount):
        raise NotImplementedError

    """Avslutar ett konto. Textuell presentation av kontots saldo ska genereras och
    #returneras."""
    def close_account(self,pnr, account_id):
        raise NotImplementedError