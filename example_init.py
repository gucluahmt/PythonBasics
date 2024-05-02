import time


class School:
    """A simple attempt to describe a school"""
    school_ID = 15
    def __init__(self,type, level):
        self.type = type
        self.level = level

    def open(self):
        print(f'The school is open')


    def school_description(self):
        print(f"{self.type} {self.level.title()} is open.")
        print(f"I'm going to {self.type} {self.level} ")
        print(f"The best school is a {self.type} {self.level}. This is my favourite")
        new_school_Id = self.school_ID + 20
        print(new_school_Id)


    def close(self):
        print("The schools are going to close on june")

my_school = School('American', 'high school')
my_school.open()
my_school.school_description()
my_school.close()

print("--------------New Example -----------------")

class City:
    """A simple attempt to describe a city"""
    def __init__(self, capital, country):
        self.capital = capital
        self.country = country

    def vacation(self):
        print(f"I'm going to {self.capital}. ")

    def visit(self):
        print(f"I will visit the {self.capital}. it's a capital of {self.country}")
        print(f'I love the {self.capital}. this is an amazing city of {self.country}. Highly recommended')
        print(f'I love the {self.capital}. this is my hometown in {self.country} ')



my_vacation = City('Roma', 'Italy')
my_vacation.vacation()
my_vacation.visit()

print('-----------== New Instance of City ==-----------')


my_vacation_2 = City('Istanbul', 'Turkey')
my_vacation_2.visit()
my_vacation_2.vacation()



my_college = School('universty', 'Lisans')
my_college.open()
my_college.school_description()



my_home_town =City('Taskent','Ozbekistan')
my_home_town.visit()



class User:
    """"A simple attempt to creat a user class"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User's first name is {self.first_name} and last name is {self.last_name}")

    def greet_user(self):
        print(f'Hello, my name is {self.first_name} {self.last_name} . Nice to meet you')

user_name = User('Ahmet', 'Guclu')
user_name.describe_user()
user_name.greet_user()

class Admin(User):
    def admin_describe(self):
        print(f"I am an admin. my name is {self.first_name} {self.last_name} ")

admin1= Admin('Ahmet', 'Guclu')
admin1.admin_describe()

time.sleep(10)
print('--------my name is ahmet------------')