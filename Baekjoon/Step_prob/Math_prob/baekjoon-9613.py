def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


t = int(input())
d = []
for i in range(t):
    d = list(map(int, input().split()))
    c = d.pop(0)
    res = 0
    for j in range(c):
       for k in range(c):
           if j < k:
            res += gcd(d[j], d[k])
    print(res)