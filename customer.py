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
