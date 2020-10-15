import math

n = input()
A = eval("*".join(input().split()))
m = input()
B = eval("*".join(input().split()))
gcd = str(math.gcd(A, B))


if len(gcd) < 9:
    print(gcd)
else:
    print(gcd[len(gcd) - 9 : len(gcd) + 1])