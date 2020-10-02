n = 1260
count = 0

res = 0
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n
    s = int(n / coin)
    res += s
    n %= coin

print(count, res)