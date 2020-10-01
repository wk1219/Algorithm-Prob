a = map(int, input().split())

a = list(a)
for i in range(0, len(a)):
    if a[i] == 0:
        break
    else:
        print(a[i])