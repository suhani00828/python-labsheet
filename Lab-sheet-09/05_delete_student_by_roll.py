# Delete a student from a sample list by roll number.
students = [{"roll": 101, "name": "Asha", "age": 19, "marks": 85}, {"roll": 102, "name": "Ravi", "age": 20, "marks": 78}]
try:
    roll = int(input("Roll number to delete: "))
    original_count = len(students)
    students = [student for student in students if student["roll"] != roll]
    print("Student deleted." if len(students) < original_count else "Student not found.")
    print("Remaining records:", students)
except ValueError:
    print("Enter a valid roll number.")
