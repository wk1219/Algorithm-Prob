def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(a[0], a[i])
    print('%d/%d' % (a[0]//g, a[i]//g))