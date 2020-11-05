n = int(input())
d = [1, 3, 5]

for i in range(3, 1000):
    d.append((d[i - 1] + (2 * d[i - 2])) % 10007)

print(d[n - 1])