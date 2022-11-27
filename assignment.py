from bank import Bank
from ui import UI
import sys
from datasource_textfile import DataSource_TextFile

def main():

    
   
    bank_instance=Bank("Swedish Bank")
    bank_instance._load()
    ui_instance=UI()
    ui_instance.Show_Welcome()
    running=True
    while(running):
           
            ui_instance.Show_Start_Menu()
            choice=ui_instance.get_input()
            match choice:
                    case "1":
                        #Show all customers
                        ui_instance.print_dict(bank_instance.customers)
                    case "2":
                        #Work with customer
                        print("Customer SSN?")
                        input_pnr=ui_instance.get_input();
                        result=bank_instance.check_if_customer_exists(input_pnr)
                        if result==True:
                            work_with_customer(input_pnr,ui_instance,bank_instance)
                        else:
                            print("That customer does not exist.")
                    case "3":
                        #Create new customer
                        print("Customer name?")
                        input_name=ui_instance.get_input();
                        print("SSN?")
                        input_pnr=ui_instance.get_input();
                        result=bank_instance.add_customer(input_name,input_pnr)
                        if result==True:
                            print("Customer successfully created.")
                        else:
                            print("Customer could not be created.")
                       
                    case "4":
                        #Edit customer
                        print("Customer SSN?")
                        input_pnr=ui_instance.get_input();
                        print("New name?")
                        input_name=ui_instance.get_input();
                        result=bank_instance.change_customer_name(input_name,input_pnr)
                        if result==True:
                            print("Customer name successfully changed.")
                        else:
                            print("That customer could not be found.")
                    case "5":
                        #Delete customer
                        print("Customer SSN?")
                        input_pnr=ui_instance.get_input();
                        result=bank_instance.remove_customer(input_pnr)
                        if result==-1:
                            print("There was an error removing that customer")
                        else:
                            print("Successfully removed customer\n")
                            print("Accounts removed:\n")
                            result=result.replace("#"," ")
                            print(result)
                    case "6":
                        #Quit
                        print("Finishing...")
                        bank_instance._save()
                        running=False

                
        
        
    return 0

def work_with_customer(pnr,ui_instance,bank_instance):
      running=True
      customers=bank_instance.get_customers()
      customer=None
      for key in customers:
        temp_customer=customers[key]
        if temp_customer.pnr==pnr:
            customer = customers[key]
      
      while(running):
            print("\nWorking with "+customer.name)
            ui_instance.show_customer_menu()
            choice=ui_instance.get_input()
            match choice:
                    case "1":
                        #Show all accounts
                        result=customer.get_all_accounts()
                        result=result.replace("#","\n")
                        if result=="":
                            print("No accounts found")
                        else:
                            print(result)
                    case "2":
                        #Work with account
                        print("Account no to work with?")
                        input_pnr=ui_instance.get_input();
                        work_with_account(customer,ui_instance,input_pnr)
                    case "3":
                        #Create new account
                        result=customer.add_account()
                        if result==-1:
                            print("Account could not be created.")
                        else:
                            print(f'Account {result} created.')
                    case "4":
                        #Remove account
                        print("Account no to remove")
                        input_pnr=ui_instance.get_input();
                        result=customer.close_account(input_pnr)
                        print(result)
                        if result==-1:
                            print("That account could not be found")
                        else:
                            print("Account removed.")
                    case "5":
                        #Go back
                        print("Going back...")
                        running=False


def work_with_account(customer,ui_instance,account_nr):
      account=customer.get_account(account_nr)
      running=True
      while(running):
            print("\nWorking with "+account.account_number)
            ui_instance.show_account_menu()
            choice=ui_instance.get_input()
            match choice:

                    case "1":
                        #Show balance
                        balance=account.get_balance()
                        print(balance)
                    case "2":
                        #Deposit money
                        print("How much to deposit?")
                        input_sum=ui_instance.get_input();
                        result=customer.deposit(account_nr,input_sum)
                        if result==True:
                            print("Money successfully deposited")
                        else:
                            print("Error: money could not be deposited")
                    case "3":
                        #Withdraw money
                        print("How much to withdraw?")
                        input_sum=ui_instance.get_input()
                        result=customer.withdraw(account_nr,input_sum)
                        if result==True:
                            print("Money successfully withdrawn")
                        else:
                            print("Error: money could not be withdrawn")
                    case "4":
                        #Go back
                        print("Going back...")
                        running=False



if __name__ == '__main__':
    sys.exit(main()) 

