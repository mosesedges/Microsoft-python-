
# this class create an object of Car with brand model and color as properties
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def ready(price):
        print(f'pay and have your car {price.brand} { price.model}')


manager = Car('Toyota', 'Highlander 2021', 'black')
print(manager.brand)
print(manager.model)
print(manager.color)

manager.ready()
print()

# this class create a Woman object with properties of breast, hip, and ass


class Woman:
    def __init__(self, breast, hip, ass):
        # constructor
        self.breast = breast
        self.hip = hip
        self.ass = ass
        # method

    def size(self):
        print(
            f'You have chest {self.breast} hip {self.hip} and bottom {self.ass}')


Naomi = Woman('big', 'medium', 'rounded')
Naomi.size()
Naomi.hip = 48  # modify object property with =<new property>
del Naomi.ass  # delete object property with the del keyword


# *****INHERITANCE*****

# parent object inherited by the student class
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.last_name + self.first_name_)

# child class inherited the above parent class placed in it parameter  with the super function it inherited the parent's init function and added year to it own parameter created it own  method which it later called.


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            f'welcome {self.first_name} {self.last_name} to the class of {self.graduationyear}')


justice = Student('Ejele', 'Justice', 2022)
justice.welcome()
