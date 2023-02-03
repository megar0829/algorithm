T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_matrix = []
    for i in range(N):
        for j in range(N):
            if i >= N-M+1 or j >= N-M+1:
                pass
            else:
                sum_num = 0
                for k in range(0, M):
                    for l in range(0, M):
                        sum_num += matrix[i+k][j+l]
                sum_matrix.append(sum_num)
    print(f'#{t} {max(sum_matrix)}')    