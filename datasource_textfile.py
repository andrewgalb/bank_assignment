from datasource import DataSource
import os
import pandas
import csv

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
        #df = pandas.read_csv('accounts.csv',sep=':')
        #print(df)
        with open('accounts.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=':', quotechar='|')
            for row in reader:
                print(row)
        

        