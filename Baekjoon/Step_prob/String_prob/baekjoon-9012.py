n = int(input())
for i in range(n):
    x = input()
    p = list(x)
    s = 0
    for i in p:
        if i == '(':
            s += 1
        elif i == ')':
            s -= 1
        if s < 0:
            print('NO')
            break
    if s > 0:
        print('NO')
    elif s == 0:
        print('YES')