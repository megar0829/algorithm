def bfs():
    que = set([])
    que.add((0, 0, arr[0][0]))
    rlt = 1
    while que:
        i, j, v_arr = que.pop()
        rlt = max(rlt, len(v_arr))
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] not in v_arr:
                    nv_arr = v_arr + arr[ni][nj]
                    que.add((ni, nj, nv_arr))
    return rlt

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
print(bfs())