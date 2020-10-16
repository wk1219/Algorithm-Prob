n = int(input())
f = [x for x in range(n + 1)]
for i in range(2, n + 1):
    f[i] = f[i - 1] + f[i - 2]
    f.append(f[i])
print(f[-1])