keys = input('Enter keys separated by spaces: ').split()
values = input('Enter values separated by spaces: ').split()
if len(keys) != len(values):
    print('Both lists must have the same length.')
else:
    print(dict(zip(keys, values)))
