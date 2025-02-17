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


# create object
p1 = Person("Joseph Mbugua", "Lecturer", "893849384", "True")
p2 = Person("Alice", "Student", "0", "True")
print(p1.fullname)
print(p2.fullname)