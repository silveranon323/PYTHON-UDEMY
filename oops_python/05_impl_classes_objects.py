class Employee:
    name="Ben"
    designation="Sales Executive"
    sales_made_this_week=6
    def has_achieved_target(self):
        if self.sales_made_this_week >= 5:
            print("Achieved the sales target.")
        else:
            print("Target has not been achieved.")

employee_one=Employee()
print(employee_one)