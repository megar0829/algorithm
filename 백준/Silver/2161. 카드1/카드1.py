N = int(input())
lst = list(range(1, N+1))
card = []
while len(lst) > 1:
    card.append(lst.pop(0))
    lst.append(lst.pop(0))
card.append(lst[0])
print(*card)