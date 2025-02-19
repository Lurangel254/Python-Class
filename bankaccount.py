class BankAccount:
    """initializer an account object using these properties"""
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
    def __str__(self):
        return f"{self.account_holder} {self.balance}"
    def deposit(self, amount):
        if amount> 0:
            self.balance += amount
            print(f"Deposited amount {amount}"
                  f"New balance: {self.balance}")
        else:
            print("Amount must be positive. Or > 0")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawing amount {amount}"
                  f"New balance: {self.balance}")
        else:
            print("insufficient funds")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


#create a bank account
name =input("Enter your name: ")
account = BankAccount(name)

#console program
while True:
    print("\n Welcome to Bank Account")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    choise = int(input("Enter your choice: "))
    if choise == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choise == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choise == 3:
        amount = float(input("Enter amount to check: "))
        account.check_balance()
    else:
        print("Invalid choice. Please try again.")
