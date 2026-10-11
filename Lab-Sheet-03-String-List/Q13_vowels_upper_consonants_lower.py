s = input('String: ')
out = ''
for ch in s:
    if ch.isalpha() and ch.lower() in 'aeiou':
        out += ch.upper()
    elif ch.isalpha():
        out += ch.lower()
    else:
        out += ch
print(out)
