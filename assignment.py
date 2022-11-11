from bank import Bank
from ui import UI
import sys
from datasource_textfile import DataSource_TextFile

def main():

    datasource=DataSource_TextFile()
   
    bank_instance=Bank("Swedish Bank")
    bank_instance.customers= datasource.get_all()
    
    running=True
    while(running):
            ui_instance=UI()
            ui_instance.Show_Start_Menu()
            choice=ui_instance.get_input()
            match choice:
                    case "1":
                        #Show all customers
                        ui_instance.print_array(bank_instance.customers)
                    case "2":
                        #Work with a customer
                        print("You chose 1")
                    case "3":
                        #Create new customer
                        print("Customer name?")
                        input_name=ui_instance.get_input();
                        print("SSN?")
                        input_pnr=ui_instance.get_input();
                        bank_instance.add_customer(input_name,input_pnr)
                      
                    case "4":
                        #Edit customer
                        print("Customer SSN?")
                        input_pnr=ui_instance.get_input();
                        bank_instance.change_customer_name(input_pnr)
                    case "5":
                        #Delete customer
                        print("Customer SSN?")
                        input_pnr=ui_instance.get_input();
                        bank_instance.remove_customer(input_pnr)
                    case "6":
                        #Delete customer
                        print("Finishing...")
                        running=False

                
        
        
    return 0

def work_with_customer(pnr,ui_instance):
      while(running):
            ui_instance.show_customer_menu()
            choice=ui_instance.get_input()
            match choice:
                    case "1":
                        #Show all accounts
                        raise NotImplementedError
                    case "2":
                        #Create new account
                        raise NotImplementedError
                    case "3":
                        #Remove account
                        raise NotImplementedError
                    case "4":
                        #Go back
                        print("Going back...")
                        running=False


def work_with_account(pnr,ui_instance):
      while(running):
            ui_instance.show_account_menu()
            choice=ui_instance.get_input()
            match choice:
                    case "1":
                        #Show balance
                        raise NotImplementedError
                    case "2":
                        #Deposit money
                        raise NotImplementedError
                    case "3":
                        #Withdraw money
                        raise NotImplementedError
                    case "4":
                        #Go back
                        print("Going back...")
                        running=False



if __name__ == '__main__':
    sys.exit(main()) 

