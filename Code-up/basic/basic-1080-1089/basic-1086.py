w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

s = (w * h * b) / 8
print("%.2f MB" % round(s/(1024*1024), 2))