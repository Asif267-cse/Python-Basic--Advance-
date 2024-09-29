class Employee:
    language = "Python"  # class attribute
    salary = 25000  # class attribute

    # Constructor (initializer)
    def __init__(self, name, salary=None, id=None):
        self.name = name  # instance attribute
        self.salary = salary if salary is not None else Employee.salary  # default to class attribute if not provided
        self.id = id  # instance attribute
    
    # Instance method
    def get_info(self):  
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")
    
    @staticmethod
    def greet():  # static method
        print("Hello, Good morning!")
# Using static method greet()
Employee.greet()  # Output: Hello, Good morning!
# Creating an object
asif = Employee(name="Asif", salary=30000, id=101)  # passing name, salary, id
asif.language = "Js"  # instance attribute overrides class attribute

# Creating another object
Sam = Employee(name="Sam", id=102)  # default salary from class attribute

# Using get_info method
asif.get_info()  # Output: Name: Asif, Language: Js, Salary: 30000
Sam.get_info()   # Output: Name: Sam, Language: Python, Salary: 25000

