marks = {'Aman': 78, 'Riya': 92, 'Karan': 65}
if marks:
    highest = max(marks, key=lambda student: marks[student])
    lowest = min(marks, key=lambda student: marks[student])
    print('Highest marks:', highest, marks[highest])
    print('Lowest marks:', lowest, marks[lowest])
