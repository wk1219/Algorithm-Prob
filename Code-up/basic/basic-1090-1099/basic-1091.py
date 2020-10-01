a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
s = a
for i in range(0, n):
    a = s
    s = a * m + d

print(a)