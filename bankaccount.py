import hashlib

# Sample user database (username: hashed password)
users_db = {
    "Joseph Mbugua": hashlib.sha256("Kenya@2024".encode()).hexdigest(),
    "Hassan Siyyad": hashlib.sha256("hp101".encode()).hexdigest(),
    "Jane Doe": hashlib.sha256("JD100".encode()).hexdigest(),
}

# Bank account details (only accessible if authenticated)
bank_accounts = {
    "Joseph Mbugua": {
        "account_number": "1234567890",
        "balance": 5000,  # Changed to float for calculations
        "account_type": "Savings"
    },
    "Hassan Siyyad": {
        "account_number": "9876543210",
        "balance": 12300,
        "account_type": "Checking"
    },
    "Jane Doe": {
        "account_number": "1029384756",
        "balance": 50000,
        "account_type": "Checking"
    }
}


class BankAccount:
    """Bank account class with deposit, withdraw, and transfer methods."""

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"{self.account_holder} - Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("❌ Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrawn ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("❌ Insufficient funds or invalid amount.")

    def transfer(self, amount, recipient):
        if isinstance(recipient, BankAccount) and 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"✅ {self.account_holder} transferred ${amount} to {recipient.account_holder}.")
            print(
                f"New balances - {self.account_holder}: ${self.balance:.2f}, {recipient.account_holder}: ${recipient.balance:.2f}")
        else:
            print("❌ Invalid transfer amount or insufficient balance.")

    def check_balance(self):
        print(f"🔹 {self.account_holder}, your current balance is: ${self.balance:.2f}")


def authenticate(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return users_db.get(username) == hashed_password


# User login
username = input("Enter your username: ")
password = input("Enter your password: ")

if authenticate(username, password):
    print("\n🔹 Login Successful! Here are your bank details:\n")
    account_info = bank_accounts.get(username)

    # Create the BankAccount object for the logged-in user
    user_account = BankAccount(username, account_info["balance"])

    print(f"Account Number: {account_info['account_number']}")
    print(f"Balance: ${user_account.balance:.2f}")
    print(f"Account Type: {account_info['account_type']}")

    # Create bank account objects for all users
    accounts = {name: BankAccount(name, details["balance"]) for name, details in bank_accounts.items()}

    while True:
        print("\n🏦 Welcome to Your Bank Account")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Transfer money")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            user_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            user_account.withdraw(amount)
        elif choice == "3":
            recipient_name = input("Enter recipient's name: ")
            if recipient_name in accounts and recipient_name != username:
                amount = float(input("Enter amount to transfer: "))
                user_account.transfer(amount, accounts[recipient_name])
            else:
                print("❌ Invalid recipient.")
        elif choice == "4":
            user_account.check_balance()
        elif choice == "5":
            print("👋 Thank you for using our banking system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

else:
    print("\n❌ Access Denied! Invalid username or password.")
