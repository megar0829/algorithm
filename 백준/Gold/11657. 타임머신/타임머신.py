# 벨만-포드 알고리즘
def bellman_ford(start):
    distance[start] = 0
    
    # N 번 edge relaxation을 반복
    # N - 1번 탐색하고 마지막 한번은 Negative cycle 존재 확인
    for i in range(1, N + 1):
        for now, next, cost in edge:
            if distance[now] != 1e9:
                if distance[next] <= distance[now] + cost:
                    continue

                distance[next] = distance[now] + cost
                
                # N 번째 반복에서 갱신되는 값이 있으면 Negative cycle 존재
                if i == N:
                    return False
    return True


N, M = map(int, input().split())

edge = [list(map(int, input().split())) for _ in range(M)]

distance = [1e9] * (N + 1)

# Negative cycle이 없는 경우
if bellman_ford(1):
    # 시작 노드를 제외한 모든 노드에서 다른 노드로 가는 최소 거리 출력
    for i in range(2, N + 1):
        # 해당 노드에 도착하지 못했다면 연결X
        if distance[i] == 1e9:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)