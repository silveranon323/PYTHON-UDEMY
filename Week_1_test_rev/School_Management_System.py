class Student:
    def __init__(self, name: str, roll_number: int, grades: dict = None):
        self.name = name
        self.roll_number = roll_number
        self.__grades = grades if grades else {}

    def add_grade(self, subject: str, score: int):
        if 0 <= score <= 100:
            self.__grades[subject] = score
        else:
            raise ValueError("Score must be 0-100")

    def get_grade(self, subject: str):
        return self.__grades.get(subject, "No grade found")

    def average_grade(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def get_all_grades(self):
        return self.__grades.copy()
def top_student(students_list):
    if not students_list:
        return []  # No students in the list
    
    # Step 1: Find the highest average
    max_avg = 0
    for student in students_list:
        avg = student.average_grade()
        if avg > max_avg:
            max_avg = avg
    
    # Step 2: Collect all students with that average (handle ties)
    top_students = []
    for student in students_list:
        if student.average_grade() == max_avg:
            top_students.append(student)
    
    return top_students

students=[]
roll_numbers=set()
for i in range(n):
    print(f"\nEntering details for student {i+1}")
    
    # Input name
    name = input("Enter student name: ")
    
    # Input roll number and check uniqueness
    while True:
        roll_number = int(input("Enter roll number: "))
        if roll_number not in roll_numbers:
            roll_numbers.add(roll_number)
            break
        else:
            print("Roll number already exists. Enter a unique roll number.")
    
    # Create Student object
    student = Student(name, roll_number)
    
    # Input grades for 3 subjects
    for j in range(3):
        subject = input(f"Enter subject {j+1} name: ")
        score = int(input(f"Enter score for {subject}: "))
        student.add_grade(subject, score)
    
    # Add student to list
    students.append(student)
# Print average of all students
print("\nStudent averages:")
for student in students:
    print(f"{student.name} (Roll: {student.roll_number}) - Average: {student.average_grade():.2f}")

# Find top student(s)
top_students = top_student(students)

print("\nTop Student(s):")
for student in top_students:
    print(f"{student.name} (Roll: {student.roll_number}) - Average: {student.average_grade():.2f}")
