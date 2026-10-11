s = input('String: ')
out = ''
for ch in s:
    if ch not in out:
        out += ch
print(out)
