T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    a = a%10
    lst_1 = []
    cnt = 1
    for i in range(b):
        save = (a**cnt)%10
        if save not in lst_1:
            lst_1.append(save)
            cnt += 1
        else:
            break
    if lst_1[(b%len(lst_1))-1] == 0:
        print(10)
    else:
        print(lst_1[(b%len(lst_1))-1])