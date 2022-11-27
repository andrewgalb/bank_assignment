# -*- coding: utf-8 -*-
from customer import Customer
from transaction import Transaction
from account import Account
from datasource import DataSource
from datasource_textfile import DataSource_TextFile
from ui import UI


"""Man ska till exempel kunna ändra kundens namn samt hämta information
om kunden (personnummer, för- och efternamn samt hämta information
om kundens konton (kontonummer, saldo, kontotyp)).
Dessutom ska man kunna hantera kundens konto(n). Implementera
metoder som säkerställer ovanstående krav i klassen Bank nedan.
(Bank inkluderar förslag på metoder. Komplettera dessa med fler metoder
om det behövs)."""
class Bank:

    customers={}
    transactions=[]

    def __init__(self,name):
        self.name=name

    """Läser in text filen och befolkar listan som ska innehålla kunderna."""
    def _load(self):
        datasource=DataSource_TextFile()
        self.customers=datasource.get_all()   

    """Läser in text filen och befolkar listan som ska innehålla kunderna."""
    def _save(self):
        datasource=DataSource_TextFile()
        datasource.serialize(self)
    
    """Returnerar bankens alla kunder (personnummer och namn)"""
    def get_customers(self):
        return self.customers

    """Skapar en ny kund med namn och personnummer. Kunden skapas endast om det inte
    finns någon kund med personnumret som angetts. Returnerar True om kunden skapades
    annars returneras False."""
    def add_customer(self,name, pnr):
        try:
            c=Customer(id=None,name=name, pnr=pnr)
            self.customers[pnr]=c
            return True
        except:
            return False
        

    """Returnerar information om kunden inklusive dennes konton. Första platsen i listan är
    förslagsvis reserverad för kundens namn och personnummer sedan följer informationen
    om kundens konton."""
    def get_customer(self,pnr):
        return self.customers[pnr]

    def check_if_customer_exists(self,pnr):
        customers=self.get_customers()
        customer=None
        for key in customers:
            temp_customer=customers[key]
            if temp_customer.pnr==pnr:
                 return True
        return False

    """Byter namn på kund, returnerar True om namnet ändrades annars returnerar det False
    #(om kunden inte fanns)."""
    def change_customer_name(self,name,pnr):
        try:
            customer=self.customers[pnr]
            customer.name=name
            return True
        except:
            return False

    """Returnerar alla transaktioner som en kund har gjort med ett specifikt
    konto eller -1 om kontot inte existerar"""
    def get_all_transactions_by_pnr_acc_nr(self,pnr, acc_nr ):
        raise NotImplementedError


    """Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton
    #tas också bort och resultatet returneras. Listan som returneras ska innehålla information
    #om alla konton som togs bort, saldot som kunden får tillbaka."""
    def remove_customer(self,pnr):
        try:
            customer=self.customers[pnr]
            result=customer.delete_accounts()
            del self.customers[pnr]
            return result
        except:
            return -1

   

   

