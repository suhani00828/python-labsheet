a, b, c = (float(input(f'Side {i}: ')) for i in range(1, 4))
if min(a, b, c) <= 0 or a + b <= c or a + c <= b or (b + c <= a):
    print('Invalid triangle')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Scalene')
