num = int(input())
time_list = []
for i in range(0, num):
    a, b = map(int, input().split())
    time_list.append((a, b))
    
time_list = sorted(time_list, key=lambda t: t[0])
time_list = sorted(time_list, key=lambda t: t[1])
last = 0
cnt = 0
for i, j in time_list:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
