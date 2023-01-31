T = int(input())
for _ in range(T):
    cnt = 0
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for x in range(m)]
    for i in range(n):
        cnt_1 = 0
        move = 0
        for j in range(m):
            if box[j][i] == 1:
                cnt_1 += 1
            else:
                move += cnt_1 
        cnt += move
    print(cnt)