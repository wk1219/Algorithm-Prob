data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1

m = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

res = 0
for n in m:
    nx = x + n[0]
    ny = y + n[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        res += 1
print(res)