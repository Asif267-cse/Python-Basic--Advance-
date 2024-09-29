class Employee:
    language = "Python"  # class attribute
    salary = 25000  # class attribute
    
    def get_info(self):  # instance method, needs self
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")
    
    @staticmethod
    def greet():  # static method, does not need self or cls
        print("Hello, Good morning!")

# Creating an object
asif = Employee()
asif.name = "Asif"  # instance attribute
asif.language = "Js"  # instance attribute overrides class attribute

# Creating another object
Sam = Employee()
Sam.name = "Sam"

# Using get_info method
asif.get_info()  # Output: Name: Asif, Language: Js, Salary: 25000
Sam.get_info()   # Output: Name: Sam, Language: Python, Salary: 25000

# Using static method greet()
Employee.greet()  # Output: Hello, Good morning!
