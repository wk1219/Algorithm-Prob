def fibo(n):
    fibo = [0, 1]
    mod = 1000000
    p = int(mod//10*15)
    i = 2
    while i < p:
        fibo.append(fibo[i - 1] + fibo[i - 2])
        fibo[i] %= mod
        i += 1
    return fibo[n % p]


n = int(input())
print(fibo(n))