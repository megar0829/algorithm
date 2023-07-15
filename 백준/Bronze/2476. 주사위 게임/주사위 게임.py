N = int(input())
price = []
for _ in range(N):
    lst = list(map(int ,input().split()))
    if lst[0] == lst[1] == lst[2]:
        price.append(10000 + (lst[0] * 1000))
    elif lst[0] == lst[1] or lst[1] == lst[2]:
        price.append(1000 + (lst[1] * 100))
    elif lst[0] == lst[2]:
        price.append(1000 + (lst[2] * 100))
    elif lst[0] != lst[1] and lst[1] !=lst[2] and lst[2] != lst[0]:
        price.append(max(lst) * 100)
print(max(price))