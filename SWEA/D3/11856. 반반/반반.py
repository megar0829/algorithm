TC = int(input())
for t in range(1, TC+1):
    word = input()
    lst = []
    cnt = 0
    for i in word:
        lst.append(i)
    for j in word:
        if lst.count(j) == 2:
            pass
        else:
            print(f'#{t} No')
            cnt += 1
            break
    if cnt == 0:
        print(f'#{t} Yes')