from string import ascii_uppercase
from string import ascii_lowercase

alpha_up = list(ascii_uppercase)
alpha_low = list(ascii_lowercase)

data = input()
data = data.lower()
alpha = []
for i in range(len(alpha_low)):
    alpha.append((alpha_low[i], 0))
alpha_dict = dict(alpha)

for i in range(len(data)):
    if data[i] in alpha_dict:
        alpha_dict[data[i]] += 1

max_val = max(alpha_dict.values())
keys = []
values = []
for key, value in alpha_dict.items():
    keys.append(key)
    values.append(value)

cnt = 0
res = ''

for i in range(len(values)):
    if max_val == values[i]:
        res = keys[i]
        cnt += 1
    if cnt > 1:
        res = '?'

if res.isupper():
    print(res.lower())
else:
    print(res.upper())