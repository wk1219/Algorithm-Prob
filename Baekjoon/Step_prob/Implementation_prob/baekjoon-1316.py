n = int(input())

res = 0
for i in range(n):
    data = input()
    for j in range(len(data)):
        if j != len(data) - 1:
            if data[j] == data[j+1]:
                continue
            elif data[j] in data[j+1:]:
                break
        else:
            res += 1
print(res)