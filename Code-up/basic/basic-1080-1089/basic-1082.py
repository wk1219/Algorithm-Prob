a = input()
s = '0x' + a
s = int(s, 16)
for i in range(0, 15):
    print("%s*%X=%X" % (a, i+1, s*(i+1)))