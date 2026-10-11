ch = input('One character: ')
print('Invalid input' if len(ch) != 1 else 'Uppercase' if ch.isupper() else 'Lowercase' if ch.islower() else 'Digit' if ch.isdigit() else 'Special character')
