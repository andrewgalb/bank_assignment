# -*- coding: utf-8 -*-
import uuid
import datetime

"""Belopp attributet kan ha negativa eller positiva nummer, t.ex., om kunden har tagit ut 2000 kr visar belopp
attributet -2000. Att sätta in 300 kr ger attributet ett värde av +300 eller 300."""
class Transaction:


    def __init__(self,customerId,accountId,amount):
        self.id=uuid.uuid4().hex
        self.customerId=customerId
        self.accountId=accountId
        self.amount=amount
        self.date=x = datetime.datetime.now()

    def __repr__(self):
        return f'Id:{self.id} Customer Id:{self.customerId} Account Id:{self.accountId} Amount:{self.amount} Date:{self.date}'
