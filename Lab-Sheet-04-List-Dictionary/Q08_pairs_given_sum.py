numbers = [int(x) for x in input('Enter integers separated by spaces: ').split()]
target = int(input('Enter target sum: '))
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
print('Pairs =', pairs)
