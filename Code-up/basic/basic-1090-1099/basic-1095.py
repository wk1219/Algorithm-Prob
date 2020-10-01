x = int(input())
a = input().split()
n = []
for i in range(0, x):
    n.append(int(a[i]))

print(min(n))