print("Welcome to the console calculator")
while True:
        print("\nchoose equation:")
        print("1. a + b + c")
        print("2. a - b + c")
        print("3. a * b * c")
        print("4. a * b / c")
        print("5. a / b % c")
        print("6. a - b / c")
        print("7. a + b / c")
        print("8. a + b % c")
        print("9. Exit")
        my_choice = input("Enter your choice: ")
        if my_choice == "1":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a + b + c")
            result = a + b + c
            print(f"{a} + {b} + {c} ={result}")
        if my_choice == "2":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a - b + c")
            result = a - b + c
            print(f"{a} - {b} + {c} ={result}")
        if my_choice == "3":
            num1 = input("enter a number: ")
            num2 = input("enter second number: ")
            num3 = input("enter third number: ")
            print("a * x * y")
            result = num1 * num2
            print(f"{num1} * {num2} * {num3} ={result}")
        if my_choice == "4":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a * b / c")
            result = a * b / c
            print(f"{a} * {b} / {c} ={result}")
        if my_choice == "5":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a / b % c")
            result = a / b % c
            print(f"{a} / {b} % {c} ={result}")
        if my_choice == "6":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a - b / c")
            result = (a - b) / c
            print(f"{a} - {b} / {c} ={result}")
        if my_choice == "7":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a + b / c")
            result = a + b / c
            print(f"{a} + {b} / {c} ={result}")
        if my_choice == "8":
            a = input("enter a number: ")
            b = input("enter second number: ")
            c = input("enter third number: ")
            print("a + b % c")
            result = a + b % c
            print(f"{a} + {b} % {c} ={result}")
        elif my_choice == "9":
            print("successfully exited")
            break  # stops the loop
        else:
            print(f"This is an invalid choice")



