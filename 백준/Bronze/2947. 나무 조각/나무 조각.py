lst = list(map(int, input().split()))
i = 0
while lst != sorted(lst):
    if lst[i] > lst[i+1]:
        save_lst = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = save_lst
        print(*lst)
    i += 1
    if i == 4:
        i = 0