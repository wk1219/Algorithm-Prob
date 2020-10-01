num_list = []

while len(num_list) < 10:
    a = int(input())
    b = a % 42
    num_list.append(b)
    out_list = list(set(num_list))  # Deduplication set
print(len(out_list))

