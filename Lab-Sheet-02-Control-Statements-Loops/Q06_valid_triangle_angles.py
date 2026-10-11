a, b, c = (float(input(f'Angle {i}: ')) for i in range(1, 4))
print('Valid triangle' if min(a, b, c) > 0 and a + b + c == 180 else 'Invalid triangle')
