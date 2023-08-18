# 행렬 내부에서 n 이 존재하는 좌표 찾아서 반환하는 함수
def find_num(n):
    for i in range(1, 98):
        for j in range(1, 98):
            if arr[i][j] == n:
                return i, j


def bfs(start, goal):  # start: 출발점 좌표, goal: 도착점 좌표
    queue = []                       # 큐 생성
    queue.append(start)              # 큐에 출발 좌표 넣기
    visited[start[0]][start[1]] = 1  # 출발 좌표 방문처리

    while queue:             # 큐가 빌때까지 반복
        i, j = queue.pop(0)  # 큐에서 좌표를 꺼냄

        for k in range(4):   # 해당 좌표에서 상하좌우 델타탐색
            ni, nj = i + di[k], j + dj[k]

            # 범위 내에서만 탐색하므로 범위제한 x
            # 미방문 상태이고 해당 좌표의 값이 1이 아니라면
            if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                queue.append((ni, nj))  # 해당 좌표 큐에 넣기
                visited[ni][nj] = 1     # 해당 좌표 방문처리

    # 만약 도착좌표의 방문처리가 되지 않았다면 (도착하지 못했다면)
    if visited[goal[0]][goal[1]] == 0:  # 0 반환
        return 0
    return 1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for _ in range(10):
    tc = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    # 행렬을 탐색할 때는 visited 도 같은 크기의 행렬로 생성
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {bfs(find_num(2), find_num(3))}')