from collections import deque
import sys
input = sys.stdin.readline


def find_room(x, y):
    que = deque([(x, y)])
    visited[x][y] = num
    cnt = 1

    while que:
        x, y = que.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            mx, my = nx + dx, ny + dy
            if 1 <= nx < 2 * N and 1 <= ny < 2 * M:
                if not arr[nx][ny] and not visited[mx][my]:
                    que.append((mx, my))
                    visited[mx][my] = num
                    cnt += 1

    return cnt

def check_room(n, m):
    save_val = input_arr[n][m]

    if save_val >= 8:
        arr[(2 * n) + 2][(2 * m) + 1] = 1
        save_val -= 8

    if save_val >= 4:
        arr[(2 * n) + 1][(2 * m) + 2] = 2
        save_val -= 4

    if save_val >= 2:
        arr[2 * n][(2 * m) + 1] = 1
        save_val -= 2

    if save_val == 1:
        arr[(2 * n) + 1][2 * m] = 2
        save_val -= 1


M, N = map(int, input().split())

arr = [[0] * ((2 * M) + 1) for _ in range((2 * N) + 1)]

input_arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        check_room(i, j)

room_start_idx = []

visited = [[0] * ((2 * M) + 1) for _ in range((2 * N) + 1)]

result_1 = 0
result_2 = 0

count_room = [0]

num = 1
for i in range(1, (2 * N) + 1, 2):
    for j in range(1, (2 * M) + 1, 2):
        if not visited[i][j]:
            cnt_room = find_room(i, j)
            result_2 = max(result_2, cnt_room)
            num += 1
            count_room.append(cnt_room)
result_1 = num - 1

result_3 = result_2
for r in range(1, N * 2):
    for c in range(1, M * 2):
        if arr[r][c] == 1:
            if visited[r - 1][c] != visited[r + 1][c]:
                room_1 = visited[r - 1][c]
                room_2 = visited[r + 1][c]

                save_val = count_room[room_1] + count_room[room_2]

                result_3 = max(result_3, save_val)

        elif arr[r][c] == 2:
            if visited[r][c - 1] != visited[r][c + 1]:
                room_1 = visited[r][c - 1]
                room_2 = visited[r][c + 1]

                save_val = count_room[room_1] + count_room[room_2]

                result_3 = max(result_3, save_val)


print(result_1)
print(result_2)
print(result_3)