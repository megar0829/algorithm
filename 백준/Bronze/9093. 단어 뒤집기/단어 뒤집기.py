T = int(input())
for i in range(T):
    text_lst = list(map(str, input().split()))
    rvs_lst = []
    for j in range(len(text_lst)):
        save_text = text_lst[j]
        rvs_lst.append(save_text[::-1])
    print(*rvs_lst, sep=' ')