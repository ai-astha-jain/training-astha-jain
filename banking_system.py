# BASE CASE (Parent class)

class Account_Details:
  def __init__(self, account_no, account_holder_name, mobile_no, email, account_type,current_balance):
    self.account_no = account_no
    self.account_holder_name = account_holder_name
    self.mobile_no = mobile_no   
    self.email = email
    self.account_type = account_type
    self.current_balance = current_balance
    
  
  def Deposit(self, deposit_amount):
    deposit_amount = float(input("Enter the amount to be deposited: "))   
    self.current_balance += deposit_amount
    print("\n Amount Deposited: ", deposit_amount)  

  def Withdrawal(self, withdraw_amount):
    withdraw_amount = float(input("Enter the amount to be withdrawn: "))
    if bank_details[account_no][account_type] == 'current':
        current()
    else:
        if self.current_balance >= withdraw_amount:
            self.current_balance -= withdraw_amount
            print("\n The amount to be withdrawn is: ",withdraw_amount)
    
    

# CHILD CLASS (inherit from parent)
class Saving_Account(Account_Details):
  def __init__(self, account_no, account_holder_name, mobile_no, email, account_type, principal):
    super().__init__(account_no, account_holder_name, mobile_no, email, account_type, current_balance)
    self.principal = principal
    self.rate = 3
    
  def calculate_simple_interest(self,time):
    return (self.principal*self.rate*time)/100
 
 
# CHILD CLASS(inherit from parent)
class Current_Account(Account_Details):
  def __init__(self, account_no, account_holder_name, mobile_no, email,account_type, minimum_amount):
    super().__init__(account_no, account_holder_name, mobile_no, email,account_type, current_balance)
    self.minimum_amount = 10000
 


bank_details = {}

def add_update_details(account_no):
  
  if account_no in bank_details:
    print(f"\n {account_no} already exists.")
    update_details = input("Do you want to update details?(yes/no): ")
    if update_details == "yes":
      account_holder_name = input("Enter the holder name:")
      mobile_no = input("Enter the mobile no: ")
      email = input("Enter the email: ")
      
      bank_details[account_no]["account_holder_name"] = account_holder_name
      bank_details[account_no]["mobile_no"] = mobile_no
      bank_details[account_no]["email"] = email
      print(f"\nUpdated details for {account_no}: ")
  else:
    print(f"\n {account_no} does not exist. Add new entry: ")
    account_holder_name = input("Enter the holder name: ")
    while True:
        mobile_no = input("Enter the mobile_no: ")
        if len(mobile_no) == 10:
            break
        else:
            continue
    email = input("Enter the email: ")
    current_balance = input("Enter the amount to deposited: ")
    account_type = input("Enter the account type(savings/current): ") 
    accountDetails = Account_Details(account_no,account_holder_name, mobile_no, email, account_type, current_balance) 
    bank_details[account_no] = {
      "account_holder_name" : accountDetails.account_holder_name,
      "mobile_no" : accountDetails.mobile_no,
      "email" : accountDetails.email,
      "account_type": accountDetails.account_type,
      "current_balance": accountDetails.current_balance
    }   
    print("\n Added new details for {account_no}: ")
    
def savings():
    principal = float(input("Enter the principal amount(current balance): "))
    SavingAccount = Saving_Account(account_no, account_holder_name, mobile_no, email, account_type,current_balance, principal)
    print("\n Choose the saving plan duration: ")
    print("\n1. 3 years")
    print("\n2. 5 years")
    print("\n3. 10 years")
    choice = int(input("Enter your chocie(1,2,3): "))  
    if choice == 1:
        time = 3
    elif choice == 2:
        time = 5
    elif choice == 3:
        time = 10
    else:
        print("Invalid choice! Please select a valid plan.")
        
    simple_interest = SavingAccount.calculate_simple_interest(time)
    total_amount = SavingAccount.principal + simple_interest
      
    print(f"\nfor {time} years annual interest rate is {SavingAccount.rate}%, simple interest on current balance of {principal} is: ",)
    print(f"\nTotal amount after {time} years will be: {total_amount}")
    
def current():
    CurrentAccount = Current_Account(account_no, account_holder_name, mobile_no, email,account_type, current_balance, minimum_amount)
    if current_balance <= minimun_amount:
        print("User can not withdraw the amount due to insufficient balance")
    else:
        if self.current_balance >= withdraw_amount:
            self.current_balance -= withdraw_amount
            print("\n The amount to be withdrawn is: ",withdraw_amount)
    
    
while True:
    print('''\n
    1. Access Account
    2. Deposit
    3. Withdrawal
    4. Interest Rate 
    5. View Accounts
    0. exit''')
    choice = int(input("Enter the choice(1/2/3/4/0): "))
    if choice == 1:
        account_no = input("Enter the account number(or type to '0' to quit): ")
        if len(account_no) == 10:
            pass
        else:
            raise ValueError("Account Number must be exactly equal to 10 digits")
        add_update_details(account_no)
        continue
    elif choice == 2:
        fetch_account_no = input("Enter the account number: ")
        if fetch_account_no in bank_details:
            accountDetails = Account_Details(account_no,account_holder_name, mobile_no, email, account_type, current_balance)
            deposit_amount = float(input("Enter the amount to be deposited"))   
            accountDetails.Deposit(deposit_amount)
        continue   
    elif choice == 3:
        fetch_account_no = input("Enter the account number: ")
        if fetch_account_no in bank_details:
            accountDetails = Account_Details(account_no,account_holder_name, mobile_no, email, account_type, current_balance)
            withdraw_amount = float(input("Enter the amount to be withdraw: "))   
            accountDetails.Withdrawal(withdraw_amount)
        continue
    elif choice == 4: 
        if account_type == 'savings':
            savings()
        continue
    elif choice == 5:
        for key, value in bank_details.items():
            print(f"{key}:{value}")
        continue    
    elif choice == 0:
        break
    else:
        continue
    add_update_details(account_no)
    

      
  
