a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
s = (a * b * c * d) / 8
print("%.1f MB" % (round(s/(1024*1024), 1)))