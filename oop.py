"""
creating a class : we use the keyword 'class' i.e
class classname:
"""

class user:
    # here I can now define my class properties
    fullname= "Joseph Mbugua"
    role_id= "Lecturer"
    staff_id= 34983498
    is_verified= True

"""
to create an object we use the name of the class followed by a parentheses() i.e. variable = user() 
"""
person1 = user() # this creates an object of the user class
print(person1.fullname)

"""
the__init__() method : this method is always executed on an object creation
the__str__() method : this method returns the string representation of the object
"""
class Person:
    def __init__(self,fullname, role_id, staff_id, is_verified):
        self.fullname = fullname
        self.role_id = role_id
        self.staff_id = staff_id
        self.is_verified = is_verified
    def __str__(self):
        return f"{self.fullname}, {self.role_id}, {self.staff_id}, {self.is_verified}"
#custom object method
    def transform_word(self):
        newword = self.fullname.upper()
        roleup = self.role_id.upper()
        result = f"{newword} , {roleup}"
        return result
# create object
p1 = Person("Joseph Mbugua", "Lecturer", "893849384", "True")
p2 = Person("Alice", "Student", "0", "True")
print(p1.fullname)
print(p2.fullname)
#how to print object methods
print(p1.transform_word())
print(p2.transform_word())
p1.fullname = "John"
print(p1)
p2.role_id = "Admin"
print(p2)
#adding a new property to objects
p1.nationality = "Kenyan"
print(p1.nationality)
#deleting object properties : use the del keyword
del p2
print(p2)
del p1.staff_id
print(p1)