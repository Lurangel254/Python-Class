def calculate_birth_year(name,age):
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
    return f"Hello {name}, you were born in this year {birth_year}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
result = calculate_birth_year(user_name,user_age)
print(result)

from datetime import datetime

def is_valid_birth_year(year):
    current_year = datetime.now().year
    if year > current_year or year < 1800:
        return False
    return True

def calculate_age(year):
    current_year = datetime.now().year
    return current_year - year

def main():
    birth_year = int(input("Enter your birth year: "))
    if is_valid_birth_year(birth_year):
        age = calculate_age(birth_year)
        print(f"Your age is: {age}")
    else:
        print("Invalid birth year. Please enter a year between 1900 and the current year.")

if __name__ == "__main__":
    main()