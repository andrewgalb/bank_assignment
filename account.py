import uuid

class Account:

    def __init__(self,account_type):
        self.account_number=uuid.uuid4().hex    #(det kan inte finnas flera konton med samma kontonummer)
        self.account_type=account_type
        self.balance=0