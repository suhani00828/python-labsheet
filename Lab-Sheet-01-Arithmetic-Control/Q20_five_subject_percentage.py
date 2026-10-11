marks = [float(input(f'Subject {i} marks /100: ')) for i in range(1, 6)]
print('Invalid marks' if any((m < 0 or m > 100 for m in marks)) else f'Percentage = {sum(marks) / 5}%')
