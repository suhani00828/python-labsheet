a = int(input('Dividend: '))
b = int(input('Divisor: '))
print('Division by zero is not allowed.' if b == 0 else f'Quotient = {a // b}, Remainder = {a % b}')
