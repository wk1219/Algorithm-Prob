x = int(input())
a = input().split()

n = []
for i in range(0, x):
    n.append(a[i])
n.reverse()
for i in range(0, len(n)):
    print(n[i], end=' ')