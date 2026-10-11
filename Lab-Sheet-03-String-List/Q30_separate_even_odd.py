nums = [int(x) for x in input('Integers: ').split()]
print('Even =', [x for x in nums if x % 2 == 0])
print('Odd =', [x for x in nums if x % 2 != 0])
