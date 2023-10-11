from copy import deepcopy

direction = {
    0: (-1, 1),
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1)
}

# 각 좌표별 (숫자, 방향) 으로 입력값을 받아준다.
arr = []
for _ in range(4):
    idx = list(map(int, input().split()))
    arr.append([[idx[0], idx[1]],[idx[2], idx[3]], [idx[4], idx[5]], [idx[6], idx[7]]])

result = 0

def dfs(shark, rlt, arr):
    global result
    
    # 결과값에 상어가 잡은 물고기의 번호를 더하고
    # 해당 위치의 번호를 0으로 만든다.
    rlt += arr[shark[0]][shark[1]][0]
    result = max(result, rlt)
    arr[shark[0]][shark[1]][0] = 0
    
    # 1 ~ 16번 물고기를 모두 탐색하며 
    for num in range(1, 17):
        # 물고기의 위치와 방향을 찾고
        x, y = -1, -1
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == num:
                    x, y = i, j
                    break
        if (x, y) != (-1, -1):
            fish_direction = arr[x][y][1]

            # 현재 방향부터 반시계 방향으로 45도씩 회전하며 
            # 처음으로 이동할 수 있는 좌표일 때
            # 두 좌표의 값을 바꾼다.
            # 만약 방향이 바뀌었을 경우를 대비해서
            # 방향을 현재 값으로 갱신해준다.
            for d in range(8):
                di, dj = direction[(fish_direction + d) % 8]
                ni, nj = x + di, y + dj
                if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) != shark:
                    arr[x][y][1] = (fish_direction + d) % 8
                    arr[x][y], arr[ni][nj] = arr[ni][nj], arr[x][y]
                    break       
    
    # 상어의 방향을 지정하고 해당 방향으로 최대 3번까지 이동하며
    # 모든 경우의 수에 대해서 재귀를 호출하며 계산
    shark_direction = arr[shark[0]][shark[1]][1]
    di, dj = direction[shark_direction]
    for n in range(1, 4):
        ni, nj = shark[0] + di * n, shark[1] + dj * n
        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0]:
            dfs((ni, nj), rlt, deepcopy(arr))

dfs((0, 0), 0, arr)

print(result)