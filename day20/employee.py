# ASSIGNMENT
# 1 employee.py — a class attribute that counts employees created

class Employee:

    # Class attributes
    company = "Google"
    employee_count = 0

    # Constructor
    def __init__(self, name, salary):

        if self.is_valid_salary(salary):
            self.name = name
            self.salary = salary
            Employee.employee_count += 1
        else:
            raise ValueError("Salary must be greater than zero!")

    # Property getter
    @property
    def salary(self):
        return self._salary

    # Property setter
    @salary.setter
    def salary(self, value):

        if value > 0:
            self._salary = value
        else:
            raise ValueError("Salary must be greater than zero!")

    # Class method
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


# Creating employee objects
employee1 = Employee("Rahul", 50000)
employee2 = Employee("Priya", 60000)
employee3 = Employee("Sumit", 100000)

# Display employee details
print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)
print(employee3.name, employee3.salary)

# Display company
print("Company:", Employee.company)

# Display employee count
print("Total Employees:", Employee.get_employee_count())

# Test salary validation
print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-500))
print(Employee.is_valid_salary(0))

# Test invalid employee creation
try:
    employee4 = Employee("Raj", -500)
except ValueError as e:
    print(e)

# Verify employee count remains unchanged
print("Final Employee Count:", Employee.get_employee_count())