class Employee:
    def set_number_of_working_hours(self):
            self.set_number_of_working_hours=40
    def display_number_of_working_hours(self):
          print(self.set_number_of_working_hours)
class Trainee(Employee):
      def set_number_of_working_hours(self):
            self.set_number_of_working_hours=50
      def reset_number_working_hours(self):
            super().set_number_of_working_hours()  
employee=Employee()
employee.set_number_of_working_hours()
employee.display_number_of_working_hours()
trainee=Trainee()
trainee.set_number_of_working_hours()
trainee.display_number_of_working_hours()
trainee.reset_number_working_hours()
trainee.display_number_of_working_hours()