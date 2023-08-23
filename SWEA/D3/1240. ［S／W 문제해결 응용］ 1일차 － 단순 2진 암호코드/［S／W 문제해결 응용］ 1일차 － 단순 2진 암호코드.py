T = int(input())
numbers = [
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int ,input())) for _ in range(N)]
    stop = False
    ni, nj = 0, 0
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if data[i][j] == 1:
                stop = True
                ni, nj = i, j - 55
                break
        if stop:
            break
        
    arr = [0] * 56 
    for j in range(56):
            arr[j] = data[ni][nj + j]
            
    result = []
    for i in range(0, 56, 7):
        save_num = ''
        for j in range(i, i + 7):
            save_num += str(arr[j])
        for k in range(10):
            if save_num == numbers[k]:
                result.append(k)
                break
            
    rlt = 0
    odd_num = 0
    for i in range(8):
        if i % 2:
            rlt += result[i]
        else:
            odd_num += result[i]
    rlt += odd_num * 3
    
    if rlt % 10 == 0:
        sum_rlt = 0
        for i in range(8):
            sum_rlt += result[i]
        print(f'#{tc} {sum_rlt}')
    else:
        print(f'#{tc} 0')