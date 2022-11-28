from datasource import DataSource
import os
import pandas
import csv
from io import StringIO
from customer import Customer
from account import Account
import json
import jsonpickle



"""DataSource klassen kräver konkreta implementationer. Ett krav är att
implementationen ska använda en textfil som datasource"""
class DataSource_TextFile(DataSource):

    path = 'accounts.csv'

    """Denna metod implementerar kopplingen till en generisk datasource. Returnerar
    en <class ‘tuple’> med en <class ‘bool’> och en <class ‘str’> t.ex., (True,
    "“Connection successful” [, datasource namn])"""
    def datasource_conn(self):
        isFile = os.path.isfile(self.path)
        return (isFile,("Connection Successful", "Connection Error")[isFile])
 
    """Returnerar alla kunder i banken."""
    def get_all(self):
        customers={}
        with open(self.path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=':', quotechar='|')
            for row in reader:
                customer=Customer(id=row[0],name=row[1],pnr=row[2])
                accounts_array=row[3:]
                accounts_string=':'.join(accounts_array)
                accounts=self.parse_transactions(accounts_string)
                customer.accounts=accounts
                customers[customer.pnr]=customer

        return customers 

    """Returnerar alla transaktioner i banken."""
    def get_all_transactions(self):
        try:
            with open('transactions.json', 'a+') as f:
                transactions = json.load(f) 
        except:
            transactions=[]
        return transactions

    """Spara alla transaktioner i banken."""
    def serialize_all_transactions(self,bank):
        with open('transactions.json', 'w') as f:
            frozen = jsonpickle.encode(bank.transactions)
            json.dumps(frozen)

    """Skriver alla kunder och sina detaljer till fil."""
    def serialize(self,bank):
        customers={}
        with open(self.path,'w',newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE,escapechar=None)
            #writer.writerows(customers)
            customers=bank.get_customers()
            for cust in customers:
                s=customers[cust].__repr__()
                acc_string=customers[cust].get_all_accounts()
                combined=s+":"+acc_string
                writer.writerow([combined])

             


    def parse_transactions(self,accounts_string):
        accounts=[]
        accounts_array=accounts_string.split("#")
        for account in accounts_array:
            details_reader=csv.reader(StringIO(account), delimiter=':', quotechar='|')
            for details in details_reader:
                recreated_account=Account(details[0],details[1],details[2])
                accounts.append(recreated_account)

        return accounts
    

        

        