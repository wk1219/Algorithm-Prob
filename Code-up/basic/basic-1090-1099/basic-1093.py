x = int(input())
a = input().split()
n = [0 for i in range(24)]

for i in range(0, x):
    n[int(a[i]) - 1] += 1

for i in range(0, 23):
    print(n[i], end=' ')