"""
functional reusabilty
you're building an e commerce order processing system, and you need to calculate discounts,taxes,and final prices for
multiple products. instead ot writing the same logic repeatedly, you'll create reusable function
"""
price= int(input("enter price: "))
discount= int(input("enter discount percentage: "))
#function to give discount
def apply_discount(p, d):
    discount_price=(p * d/ 100)
    return p - discount_price

apply_discount(price, discount)
print(apply_discount(price, discount))

#function to calculate tax afetr discount application
def calculate_taxes(price):
    """calculate taxes based on price"""
    vattax=4.5
    result=price * (vattax/ 100)
    return result

#this function will then get our final price
def calculate_final_price(price, discount):
    """calculate final price(discount price + vattax)"""
    discount_price= apply_discount(price, discount)
    tax= calculate_taxes(discount_price)
    result= discount_price + tax
    return(f"the item discount price is {discount_price} it has a tax"
           f"of {tax} and a final price of {result}")

print(calculate_final_price(price, discount))
"""PROGRAM 2:
SCENARIO:
You're building a banking application where users can deposit, withdraw, and check balance.
instead of writing the operation multiple times, you'll create reusable function"""

amount= 0
balance= int(input("enter balance: "))
#deposit function
def deposit(balance, amount):
    result= balance + amount
    return result
#withdrawal
def withdraw(withdrawal_amount):
    withdrawal_amount= int(input("enter withdrawal amount: "))
    current_balance= deposit(balance, amount)
    if current_balance < withdrawal_amount:
        print("Insufficient funds")
    else:
        available_balance= current_balance - withdrawal_amount
        return (f"withdrawal success {withdrawal_amount} balance was at"
                f"{current_balance} new balance is {available_balance}")
print(withdraw(amount))