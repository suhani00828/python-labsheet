p = float(input('Principal: '))
r = float(input('Rate (%): '))
t = float(input('Time in years: '))
si = p * r * t / 100
print('Simple interest =', si, 'Total =', p + si)
