def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lsm(a, b):
    return (a * b) // gcd(a, b)


a, b = map(int, input().split())
print(gcd(a, b))
print(lsm(a, b))