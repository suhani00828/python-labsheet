# Display all records in the example student list.
students = [{"roll": 101, "name": "Asha", "age": 19, "marks": 85}, {"roll": 102, "name": "Ravi", "age": 20, "marks": 78}]
if students:
    for student in students:
        print(student)
else:
    print("No student records.")
