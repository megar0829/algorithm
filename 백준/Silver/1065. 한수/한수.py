def hannumber(n):
    if n > 10:
        han_lst =[]
        save_num = []
        for i in range(len(str(n))):
            han_lst.append(int(str(n)[i]))
        for j in range(1, len(str(n))):
            dif_num = han_lst[j] - han_lst[j-1]
            save_num.append(dif_num)
        if (sum(save_num) / len(save_num)) == dif_num:
            return True
N = int(input())
cnt_lst = []
for i in range(1, N+1):
    if i > 10:
        if hannumber(i) == True:
            cnt_lst.append(i)
    else:
        cnt_lst.append(i)
print(len(cnt_lst))