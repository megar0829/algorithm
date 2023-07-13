T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*3 for _ in range(N)]
    lst = []
    for i in range(N):
        save_lst = ''
        for j in range(N-1, -1, -1):
            save_lst += str(matrix[j][i])
        lst.append(save_lst)    
    for i in range(N-1, -1, -1):
        save_lst = ''
        for j in range(N-1, -1, -1):
            save_lst += str(matrix[i][j])
        lst.append(save_lst)    
    for i in range(N-1, -1, -1):
        save_lst = ''
        for j in range(N):
            save_lst += str(matrix[j][i])
        lst.append(save_lst)
    cnt = 0
    for i in range(3):
        for j in range(N):
            result[j][i] = lst[cnt]
            cnt += 1
    print(f'#{t}')
    for i in range(N):
        print(*result[i])