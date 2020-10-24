x = int(input())

s = 0
while x != 0:
    if x % 2 == 1:
        s += 1
    x = x // 2
print(s)
