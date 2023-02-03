T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        text_cnt = 0
        for j in range(N):
            if matrix[i][j] == 0:
                if text_cnt == K:
                    cnt += 1
                    text_cnt = 0
                else:
                    text_cnt = 0
            else:
                text_cnt += 1
                if j == N-1 and text_cnt == K:
                    cnt += 1
    for i in range(N):
        text_cnt = 0
        for j in range(N):
            if matrix[j][i] == 0:
                if text_cnt == K:
                    cnt += 1
                    text_cnt = 0
                else:
                    text_cnt = 0
            else:
                text_cnt += 1
                if j == N-1 and text_cnt == K:
                    cnt += 1
    
    print(f'#{t} {cnt}')