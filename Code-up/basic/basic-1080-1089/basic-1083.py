x = int(input())
for i in range(0, x):
    if (i+1) % 3 == 0:
        print("X", end=' ')
    else:
        print(i+1, end=' ')