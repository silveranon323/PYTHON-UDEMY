class Employee:
    def employee_details(self):
        self.name="Hem"
        print(self.name)

    @staticmethod
    def welcome_message():
        print("Welcome to the organistation")
employee=Employee()
employee.employee_details()
employee.welcome_message()