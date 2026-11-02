# Update a student's marks in a sample list using their roll number.
students = [{"roll": 101, "name": "Asha", "age": 19, "marks": 85}, {"roll": 102, "name": "Ravi", "age": 20, "marks": 78}]
try:
    roll = int(input("Roll number: "))
    marks = float(input("New marks: "))
    student = next((item for item in students if item["roll"] == roll), None)
    if student:
        student["marks"] = marks
        print("Marks updated:", student)
    else:
        print("Student not found.")
except ValueError:
    print("Enter a valid roll number and numeric marks.")
