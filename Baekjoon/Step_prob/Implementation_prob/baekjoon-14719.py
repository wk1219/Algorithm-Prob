a, b = map(int, input().split())
s = list(map(int, input().split()))

cnt = 0

for i in range(len(s)):
    left = max(s[:i+1])
    right = max(s[i:])
    r = min(left, right)
    cnt += abs(s[i] - r)

print(cnt)