class bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account1 = bankaccount(10000)
print(account1.balance)
# even in encapsulation our object can stil add new properties
account1.balance = 000
print(account1.balance)