class Bank():
    accounts = []
    details = dict({})
    account_number = 101

    def add_account(self,name,age,balance):
                    
            self.details = {
                "Account_number":self.account_number,
                "Name":name,
                "Age":age,
                "Balance":balance
            }
            self.accounts.append(self.details)
            self.account_number += 1

    def show_account(self):
        print()
        print()
        print("***********************ACCOUNTS************************")
        print()
        print()
        if self.accounts != []:
            for i in self.accounts:
                print(i)
            # print(self.accounts)
        else:
            print("No account exists")
    
class Transactions(Bank):
    def withdraw(self,acc,amount):
        if amount <  acc['Balance']:
            acc['Balance'] -= amount
            print(f"You have successfully withdrawn Rs {amount} from your account")
        else:
            print("Sorry, you dont have enough amount in your account to withdraw.")
            print(f"Remaining balance is {acc['Balance']} only.")
            
    def deposit(self,acc,amount):
        acc['Balance'] += amount
        
    def check_balance(self,acc):
        print(f"you have Rs {acc['Balance']} in your account")

user = Transactions()
while(True):
    print()
    print()
    print("***********************WELCOME TO BANK************************")
    print()
    print()
    print("Press 1 to create an account")
    print("Press 2 to use an account")
    print("Press 3 to show Accounts")
    print()
    print()
    choice = int(input("Enter the choice: "))

    if choice == 1:
        print("             --Fill the details--")
        name = input("              Enter the name : ")
        age = int(input("              Enter the age : "))
        balance = int(input("             Enter the amount you want to deposit : "))
        user.add_account(name,age,balance)
        
    elif choice == 2:
        acc_num = int(input("Enter your account number : "))
        for acc in user.accounts:
            if acc["Account_number"] == acc_num:
                print()
                print()
                print(f"***********************WELCOME {acc['Name']}************************")
                print()
                print()
                while(True):
                    print()
                    print()
                    print("Press 1 to Withdraw")
                    print("Press 2 to Deposit")
                    print("Press 3 to Check Balance")
                    print("Press 4 to go back")
                    print()
                    print()
                    
                    choice_2 = int(input("Enter your choice: "))
                    if choice_2 == 1:
                        withdraw = int(input("Enter the amount you wanna withdraw : "))
                        user.withdraw(acc,withdraw)
                        pass
                    elif choice_2 == 2:
                        amt = int(input("Enter the amount you want to deposit : "))
                        user.deposit(acc,amt)
                    elif choice_2 == 3:
                        user.check_balance(acc)
                    elif choice_2 == 4:
                        break
                    else:
                        print("You had entered wrong number.")                    

            else:
                print("Account does not exists")
        

    elif choice == 3:
        user.show_account()