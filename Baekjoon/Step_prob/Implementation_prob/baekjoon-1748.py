n = input()
cnt = 0
length = len(n)

for i in range(length - 1):
    cnt += 9 * (10 ** i) * (i + 1)

cnt += (int(n) - (10 ** (length - 1)) + 1) * length
print(cnt)
