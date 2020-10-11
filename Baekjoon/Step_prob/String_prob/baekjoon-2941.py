s = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for r in alpha:
    s = s.replace(r, '*')

print(len(s))