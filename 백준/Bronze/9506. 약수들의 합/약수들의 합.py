while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    lst = sorted(lst)
    if sum(lst) == n:
        print(f'{n} = {lst[0]}', *lst[1:],sep=' + ')
    else:
        print(f'{n} is NOT perfect.')