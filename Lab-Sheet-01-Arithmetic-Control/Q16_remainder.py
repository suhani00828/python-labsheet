a = int(input('Dividend: '))
b = int(input('Divisor: '))
print('Cannot divide by zero' if b == 0 else 'Remainder = ' + str(a % b))
