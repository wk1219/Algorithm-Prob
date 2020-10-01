x = int(input())
s = 0
for i in range(0, x):
    s += (i+1)
    if x <= s:
        print(s)
        break