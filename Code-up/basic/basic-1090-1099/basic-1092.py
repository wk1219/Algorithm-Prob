a, b, c = input().split()

day = 1
a = int(a)
b = int(b)
c = int(c)
while (day % a != 0) or (day % b != 0) or (day % c != 0):
    day += 1
print("%d" % day)