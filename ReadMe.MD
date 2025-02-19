NON PRIMITIVE (SEQUENCES IN PYTHON)
1. List : ordered mutable collection
variablename = ["apple","banana","cherry"]
2. Tuple :ordered ,immutable collection
variablename =[ 10.04, 30.05]
3. Range : sequence of numbers
variablename =range(5)
4. Set : collection of unique items
variablename = {1,2,3,4,5,6}
5. Dictionary : key and value pairs 
variablename = { 
                 key:value
               }
6. comparison operators
    a. == equal to
    b. != not equal to
    c. > greater than
    d. < less than
    e. >= greater than or equal to
    f. <= less than or equal to

logical operator
    a. and :: & ::returns true if both condition are true
    b. or :: ! ::returns true if one condition is met
    c. not :: ! ::reverses the result

assignment operators
    a. = : assign
    b. += :add and assign
    c. -= :subtract and assign
    d. *= :multiply and assign
    e. /= :divide and assign
    f. %= :modulus and assign

identity operator
    a. is :returns true if both comparison refer to the same object
    b. is not :returns true if they refer to different object

1.local scope
    variables defined in this scope can be accessed

### OOP (OBJECT ORIENTED PROGRAMING)
-everything in python is an object
-an object is a stand alone entity that has its own properties and methods(functions implemented to the variables)

### Building blocks of OOP
1. CLASSES OR CLASS:: is the blueprint for creating an object
2. Object:: an instance or creation of a class

### pillars of oop
1. Inheritance:: allows us to define a class and inherit all the methods and properties in another class
2. Encapsulation :: bundling of data and methods into one unit (class)
- protect data from direct access or modification outside the class
- Achieved by access modifiers
  a. public : accessible everywhere
  b. _protected : hint that it should not be accessed directly
  c. __private : Name-mangled to prevent modification
3. Abstraction : hiding complex implementation details and exposing only the relevant one.
4. Polymorphism : allows different classes to have method with the same name but different implementation: overide.
   -achieved via method over riding and duck typing.