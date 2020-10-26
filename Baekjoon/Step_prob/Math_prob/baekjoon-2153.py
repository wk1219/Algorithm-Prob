from string import ascii_lowercase
from string import ascii_uppercase

low_list = list(ascii_lowercase)
up_list = list(ascii_uppercase)
alpha_list = low_list + up_list

s = list(input())
cnt = 0


def isPrime(num):
    if num < 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(len(s)):
    if s[i] in alpha_list:
        cnt += alpha_list.index(s[i]) + 1

if isPrime(cnt):
    print("It is a prime word.")
else:
    print("It is not a prime word.")