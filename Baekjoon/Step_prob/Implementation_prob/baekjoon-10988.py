data = list(input())

res = ''
for i in range(len(data)):
    res += data[i]

re_res = ''
data.reverse()
for i in range(len(data)):
    re_res += data[i]

if res == re_res:
    print(1)
else:
    print(0)