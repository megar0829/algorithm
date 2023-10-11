import sys
input = sys.stdin.readline

# 해당 노드 방문처리 후 연결되어 있는 모든 노드를 탐색
# 이미 방문했던 노드가 있다면 False (이미 이전에 연결된 상태)
# 모두 처음 방문한다면 True
def dfs(prev, node):
    visited[node] = 1
    for next in tree[node]:
        if next != prev:
            if visited[next] or not dfs(node, next):
                return False
    return True

T = 0
while True:
    T += 1
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    
    # 연결 리스트 생성
    tree = [[] for _ in range(n + 1)]
    for _ in range(m):
        f, t = map(int, input().split())
        tree[f].append(t)
        tree[t].append(f)
    
    # 방문리스트 생성
    visited = [0] * (n + 1)
    
    # 미방문 상태거나 연결된 모든 노드를 방문처리했으면 개수 + 1
    result = 0
    for node in range(1, n + 1):
        if not visited[node] and dfs(0, node): 
            result += 1
            
    if result == 0:
        print(f'Case {T}: No trees.')
    elif result == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: A forest of {result} trees.')