# Search a sample list of students by name, ignoring case.
students = [{"roll": 101, "name": "Asha", "age": 19, "marks": 85}, {"roll": 102, "name": "Ravi", "age": 20, "marks": 78}]
target = input("Student name to search: ").strip().casefold()
matches = [student for student in students if student["name"].casefold() == target]
print(*matches, sep="\n") if matches else print("Student not found.")
