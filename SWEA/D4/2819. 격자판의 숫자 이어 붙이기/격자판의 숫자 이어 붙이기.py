def backTracking(cnt, x, y):
    global s
    if cnt == 6:
        result.add(s)
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            save_s = s[:]
            s += str(arr[nx][ny])
            backTracking(cnt + 1, nx, ny)
            s = save_s[:]


T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            s = str(arr[i][j])
            backTracking(0, i, j)
    print(f'#{tc} {len(result)}')