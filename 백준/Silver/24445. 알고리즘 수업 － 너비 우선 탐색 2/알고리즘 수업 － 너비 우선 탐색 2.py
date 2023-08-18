import sys
input = sys.stdin.readline


def bfs(start):
    visited = [0] * (N + 1)         # 방문 리스트 생성
    que = []                        # 큐 생성
    que.append(start)               # 큐에 출발점 넣기
    visited[start] = 1              # 출발점 방문처리
    result = [0] * (N + 1)          # 순서를 담을 배열 생성
    cnt = 1                         # 순서를 셀 변수

    while que:                      # 큐가 빌때까지 반복
        t = que.pop(0)              # 큐에서 앞에값 빼오기
        result[t] = cnt             # 해당 t 값의 순서 저장
        cnt += 1                    # 순서 1 증가

        for w in sorted(arr[t], reverse=True):            # 해당 t 값의 인접리스트 탐색
            if visited[w] == 0:     # 방문하지 않았다면,
                que.append(w)       # 큐에 넣고
                visited[w] = 1      # 방문처리

    return result                   # 순서 배열 반환


N, M, R = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]

# 인접 리스트 생성 - 무방향
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

# 인접리스트 정렬(내림차순)
# for i in range(N):
#     arr[i].sort(reverse=True)

for i in bfs(R)[1:]:
    print(i)