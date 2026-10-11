nums = input('Items separated by spaces: ').split()
out = []
for x in nums:
    if x not in out:
        out.append(x)
print(out)
