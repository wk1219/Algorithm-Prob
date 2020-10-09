x = []
for i in range(5):
    x.append(list(input()))
res = ''
for i in range(15):
    for j in range(5):
        if i >= len(x[j]):
            continue
        else:
            res += x[j][i]
print(res)