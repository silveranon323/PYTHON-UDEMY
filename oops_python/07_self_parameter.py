class Employee:
    def employee_details(self):
        self.name="Mathew"
        print("Name:",self.name)
        age=30
        print("Age:", age)
    def print_employee_details(self):
        print("Printing in another method")
        print("Name:",self.name)
        print("age: ",age)


employee=Employee()
print(employee.print_employee_details())