day = "Tuesday"
match day:
    case "Monday":
        print("Start of the workweek.")
    case "Friday":
        print("Weekend is here.")
    case "sunday":
        print("Time to relax!")
    case _:
        print("Just another day.")



fruits=["mango","banana","apple"]
for fruit in fruits:
    print(f"My favourite fruit is: {fruit}")


x = 0
while x < 5:
    print(x)
    x += 1



for i in fruits:
    pass
for i in fruits:
    if i =="apple":
        break
    print(i)
for i in fruits:
    if i =="banana":
        continue
    print(i)




