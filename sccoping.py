##GLOBAL SCOPE :: VARIABLE DEFINED OUTSIDE FUNCTIONS: THEY ARE ACCESSIBLE ANYWHERE IN THE FILE
myName="joseph"

##LOCAL SCOPE
def my_function():
    x = 10
    return f"{myName} defined the variable {x} as a local scope"

print(my_function())
print(myName)

##enclosing scope
def outer():
    y= 20
    def inner():
        nonlocal y
        y+=5
        return y
    inner()
    print(y)
outer()