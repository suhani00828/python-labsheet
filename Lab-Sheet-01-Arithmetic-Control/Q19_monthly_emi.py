p = float(input('Loan amount: '))
annual = float(input('Annual interest rate (%): '))
n = int(input('Months: '))
r = annual / 1200
if p < 0 or n <= 0 or annual < 0:
    print('Invalid input')
elif r == 0:
    print('Monthly EMI =', p / n)
else:
    print('Monthly EMI =', round(p * r * (1 + r) ** n / ((1 + r) ** n - 1), 2))
