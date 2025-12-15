class Employee:
    def __init__(self,name):
        self.name=name
    # def enter_employee_details(self):
    #     self.name="Marks"
    def display_employee_details(self):
        print(self.name)
employee=Employee("Mark")
employee2=Employee("Hem Kishore Pradhan")
employee.display_employee_details()
employee2.display_employee_details()