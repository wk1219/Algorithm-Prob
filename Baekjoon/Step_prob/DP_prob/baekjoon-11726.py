n = int(input())
d = [1, 2]

for i in range(2, 1000):
    d.append((d[i - 2] + d[i - 1]) % 10007)

print(d[n - 1])