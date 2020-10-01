num = int(input())

even = num//2
odd = num - num//2
for i in range(num):
    print('* ' * odd)
    print(' *' * even)