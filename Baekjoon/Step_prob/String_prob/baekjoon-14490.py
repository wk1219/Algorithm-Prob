def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


n, m = input().split(':')
g = gcd(int(n), int(m))
print("%d:%d" % (int(n) // g, int(m) // g))