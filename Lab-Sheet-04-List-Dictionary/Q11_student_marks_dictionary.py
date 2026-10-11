students = {}
count = int(input('How many students? '))
for _ in range(count):
    name = input('Student name: ')
    marks = float(input('Marks: '))
    students[name] = marks
print('Student marks =', students)
