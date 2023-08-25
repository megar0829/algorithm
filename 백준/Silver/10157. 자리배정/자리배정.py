C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
elif K == 1:
    print(1, 1)
else:
    arr = [[0] * C for _ in range(R)]
    delta = {'down': (1, 0),
             'up': (-1, 0),
             'right': (0, 1),
             'left': (0, -1)
             }
    direc = {'down': 'right',
            'right': 'up',
            'up': 'left',
            'left': 'down'
            }
    save_dir = 'down'
    i, j = 0, 0
    num = 1
    arr[i][j] = num
    check = 0
    stop_sign = True
    while stop_sign:
        ni = i + delta[save_dir][0]
        nj = j + delta[save_dir][1]
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] == 0:
                num += 1
                arr[ni][nj] = num
                if num == K:
                    print(nj + 1, ni + 1)
                    stop_sign = False
                    break
                i, j = ni, nj
                check = 0
            else:
                if check > 2:
                    break
                check += 1
                save_dir = direc[save_dir]
        else:
            save_dir = direc[save_dir]
