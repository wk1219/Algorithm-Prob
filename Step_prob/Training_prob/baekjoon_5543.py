burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
cola = int(input())
cider = int(input())

if burger1 >= burger2:
    if burger2 >= burger3:
        min = burger3
    elif burger2 <= burger3:
        min = burger2
elif burger2 >= burger3:
    if burger3 >= burger1:
        min = burger1
    elif burger3 <= burger1:
        min = burger3

if cola >= cider:
    beverage_min = cider
else:
    beverage_min = cola

total = int(min) + int(beverage_min) - 50
print(int(total))