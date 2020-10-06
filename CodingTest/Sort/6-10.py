n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

s = sorted(s, reverse=True)
for i in s:
    print(i, end=' ')