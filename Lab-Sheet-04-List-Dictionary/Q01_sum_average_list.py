numbers = [float(x) for x in input('Enter numbers separated by spaces: ').split()]
if numbers:
    total = sum(numbers)
    print('Sum =', total)
    print('Average =', total / len(numbers))
else:
    print('No numbers entered.')
