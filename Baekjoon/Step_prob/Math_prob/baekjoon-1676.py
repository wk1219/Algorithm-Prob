n = int(input())

res = 1
cnt = 0

for i in range(1, n + 1):
    res *= i

for n in str(res)[::-1]:
    if n == '0':
        cnt += 1
    else:
        break
print(cnt)
