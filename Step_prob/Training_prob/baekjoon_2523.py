num = int(input())

for i in range(1, 2*num):
    for j in range(0, 1):
        if i > (2*num)/2:
            print('*'*(2*num - i))
        else:
            print('*'*i)


