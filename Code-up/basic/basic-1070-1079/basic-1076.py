x = input()
for i in range(ord(x) - ord('a'), -1, -1):
    print(chr(ord(x)-i), end=' ')
