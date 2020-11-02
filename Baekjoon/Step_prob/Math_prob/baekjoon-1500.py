s, k = map(int, input().split())

x = s // k
y = s % k
z = 1
while k > 0:
    if y > 0:
        z *= x + 1
        y -= 1
    else:
        z *= x
    k -= 1
print(z)