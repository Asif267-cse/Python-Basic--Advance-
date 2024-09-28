# Diagram of inheritance:
#          Company
#             |
#         Employee
#             |
#        Programmer
#
# Company -> Parent class, has the attribute company_name
# Employee -> Inherits from Company, has attributes name, id, and salary
# Programmer -> Inherits from Employee, adds the language attribute and get_info method

class Company:
    company_name = "Google"  # Attribute for company name

class Employee(Company):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

class Programmer(Employee):
    def __init__(self, name, id, salary, language):
        super().__init__(name, id, salary)  # Call parent constructor
        self.language = language

    def get_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Language: {self.language}, Company: {self.company_name}")

# Create instances of Programmer
asif = Programmer("Asif", 123, 50000, "Python")
alex = Programmer("Alex", 456, 60000, "Java")

# Call the get_info method for both objects
asif.get_info()
alex.get_info()
