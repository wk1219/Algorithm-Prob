n = list(map(int, input().split()))
v = 0
for i in n:
    v += i*i
print(v % 10)