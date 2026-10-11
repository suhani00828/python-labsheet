numbers = [float(x) for x in input('Enter numbers separated by spaces: ').split()]
result = [x for x in numbers if x >= 0]
print('List without negative numbers =', result)
