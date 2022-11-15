
class UI:

    def Show_Start_Menu(self):
        print("***********\n")
        print("Welcome to the Bank.")
        print("Please choose an option:")
        print("1:Show customers")
        print("2:Work with a customer")
        print("3:Create new customer")
        print("4:Edit customer")
        print("5:Delete customer")
        print("6:Exit")

    def show_customer_menu(self):
        print("***********\n")
        print("Customer Menu.")
        print("Please choose an option:")
        print("1:Show accounts")
        print("2:Work with an account")
        print("3:Add an account")
        print("4:Remove an account")
        print("5:Go back")

    def show_account_menu(self):
        print("***********\n")
        print("Account Menu.")
        print("Please choose an option:")
        print("1:Show balance")
        print("2:Deposit money")
        print("3:Withdraw money")
        print("4:Go back")

    def get_input(self):
        text=input()
        return text

    def print_array(self,array_to_print):
        for val in array_to_print:
            print(val.__repr__())

    def print_dict(self,dict_to_print):
        for key in dict_to_print:
            print(dict_to_print[key])
