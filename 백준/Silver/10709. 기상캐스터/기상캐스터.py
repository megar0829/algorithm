H, W = map(int, input().split())
data = [list(input()) for _ in range(H)]
arr = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if data[i][j] == '.':
            if j == 0:
                arr[i][j] = -1
            else:
                cnt = 1
                check = False
                while j - cnt >= 0:
                    if data[i][j - cnt] == 'c':
                        check = True
                        break
                    cnt += 1
                if check:
                    arr[i][j] = cnt
                else:
                    arr[i][j] = -1
for i in range(H):
    print(*arr[i])
