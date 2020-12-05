n = int(input())
data = [list(input().split()) for _ in range(n)]
for i in range(n):
    for j in data[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()