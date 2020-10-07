n = list(input())
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [0] * 10

for i in n:
    idx = int(i)
    if idx == 9:
        idx = 6
    res[idx] += 1
res[6] = (res[6] + 1) // 2
print(max(res))