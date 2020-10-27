n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.sort()
for i in range(len(s)):
    print(s[i])