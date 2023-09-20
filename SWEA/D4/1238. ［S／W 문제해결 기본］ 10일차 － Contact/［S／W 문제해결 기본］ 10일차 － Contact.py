def bfs(start):
    visited = [0] * 101          # 방문 리스트 생성
    queue = []                   # 큐 생성
    queue.append(start)          # 큐에 출발점 넣기
    visited[start] = 1           # 출발점 방문표시

    while queue:                 # 큐가 빌때까지 반복
        t = queue.pop(0)         # 큐에서 값을 꺼내기

        for w in arr[t]:         # 해당 값의 인접리스트 탐색
            if visited[w] == 0:  # 미방문 상태라면
                queue.append(w)  # 값을 큐에 넣기

                # 방문처리 값을 이동거리로 사용하기 위해 이전 방문 값 + 1
                visited[w] = visited[t] + 1

    return visited               # 방문 리스트 반환


def find_max(visited):
    # 방문값 중 최댓값을 찾기
    max_val = max(visited)
    # 최대값을 갖는 값들의 index 를 담은 배열 생성
    max_lst = []
    for i in range(101):
        if visited[i] == max_val:
            max_lst.append(i)
    return max_lst[-1]  # 가장 뒤에 있는 값(최대 index) 반환


for tc in range(1, 11):
    N, start = map(int, input().split())
    E = list(map(int, input().split()))

    # 인접 리스트 생성
    arr = [[] for _ in range(101)]
    for i in range(0, len(E), 2):
        if E[i + 1] not in arr[E[i]]:
            arr[E[i]].append(E[i + 1])
    print(f'#{tc} {find_max(bfs(start))}')