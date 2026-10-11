for n in range(2, 101):
    prime = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            prime = False
            break
    if prime:
        print(n, end=' ')
print()
