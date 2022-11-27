import uuid
from transaction import Transaction
from account import Account

class Customer:

    accounts=[]
    transactions=[]

    def __init__(self,id, name,pnr):
        if id==None:
              self.id=uuid.uuid4().hex[:8]
        else:
            self.id=id
        self.name=name
        self.pnr=pnr  

    def __str__(self):
        return f'{self.id} {self.name} {self.pnr}'

    def __repr__(self):
        return f'{self.id}:{self.name}:{self.pnr}'

    """Skapar ett konto till kunden med personnumret som angetts, returnerar kontonumret som
    det skapade kontot fick alternativt returneras –1 om inget konto skapades."""
    def add_account(self):
        try:
            account=Account(account_number=None,account_type="debit account",balance=0)
            self.accounts.append(account)
            return account.account_number
        except:
            return -1

    """Returnerar Textuell presentation av kontot med kontonummer som tillhör
    #kunden (kontonummer, saldo, kontotyp)."""
    def get_account(self, account_id):
        acc= next((x for x in self.accounts if x.account_number==account_id),None)
        return acc

    """Returnerar Textuell presentation av kontot med kontonummer som tillhör
    #kunden (kontonummer, saldo, kontotyp)."""
    def get_all_accounts(self):
        combined_string=""
        for acc in self.accounts:
            combined_string+=acc.__str__()
            combined_string+='#'
        combined_string=combined_string[:-1]
        return combined_string

    """Gör en insättning på kontot, returnerar True om det gick bra annars False."""
    def deposit(self,account_id, amount):
        try:
            account=[x for x in self.accounts if x.account_number==account_id]
            if len(account)==0:
                return False
            result=account[0].deposit(amount)
            return result
        except:
            return False

    """Gör ett uttag på kontot, returnerar True om det gick bra annars False."""
    def withdraw(self, account_id, amount):
          try:
            account=[x for x in self.accounts if x.account_number==account_id]
            if len(account)==0:
                return False
            result=account[0].deposit(-(float)(amount))
            return result
          except:
            return False

    def delete_accounts(self):
        concat_string=""
        for a in self.accounts:
            concat_string+=(self.close_account(a.account_number)+"\n")
        return concat_string

    """Avslutar ett konto. Textuell presentation av kontots saldo ska genereras och
    #returneras."""
    def close_account(self, account_id):
        try:
            account=[x for x in self.accounts if x.account_number==account_id]
            if len(account)==0:
                return -1
            text_rep=account[0].__repr__()
            self.accounts=[x for x in self.accounts if x.account_number != account_id]
            return text_rep
        except:
            return -1