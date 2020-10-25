n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
for i in range(n):
    b.append(a[i] * (i + 1))
print(max(b))