w = float(input('Weight in kg: '))
h = float(input('Height in metres: '))
print('Invalid measurements' if w <= 0 or h <= 0 else f'BMI = {w / (h * h):.2f}')
