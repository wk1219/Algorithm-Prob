n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a, reverse=True)
b = sorted(b)


res = 0
for i in range(n):
    k = a[i] * b[i]
    res += k

print(res)