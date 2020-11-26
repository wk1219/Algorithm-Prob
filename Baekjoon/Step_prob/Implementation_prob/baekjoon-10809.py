data = input()
alpha = list(range(97, 123))

for x in alpha:
    print(data.find(chr(x)), end=' ')