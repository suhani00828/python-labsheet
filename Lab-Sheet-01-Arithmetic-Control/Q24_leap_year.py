y = int(input('Year: '))
print('Leap year' if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 'Not a leap year')
