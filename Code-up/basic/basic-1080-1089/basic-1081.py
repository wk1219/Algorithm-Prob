a, b = input().split()
a = int(a)
b = int(b)
for i in range(0, a):
    for j in range(0, b):
        print("%d %d" % (i+1, j+1))