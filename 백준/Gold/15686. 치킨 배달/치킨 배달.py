import sys
input = sys.stdin.readline


# 치킨 거리 계산 함수
def len_chicken(i):
    global min_len_city_chicken
    # 도시의 치킨 거리
    len_city_chicken = 0
    
    # 도시의 모든 집을 탐색하며 치킨 거리를 계산 후
    # 각 집의 치킨거리를 모두 더해서 도시의 치킨 거리 찾기
    for h in range(home_idx):
        # 집의 치킨거리
        min_len = 1e9
        for c in range(i + 1):
            min_len = min(min_len, abs(home[h][0] - chicken_lst[c][0]) + abs(home[h][1] - chicken_lst[c][1]))
        len_city_chicken += min_len
    # 도시의 치킨거리의 최소값 갱신
    min_len_city_chicken = min(min_len_city_chicken, len_city_chicken)


def backTracking(i, depth):
    if i == M:
        return
    
    for idx in range(depth, chicken_idx):
        if not used[idx]:
            # 재귀 호출 전 로직
            used[idx] = 1
            chicken_lst.append(chicken[idx])
            
            # 재귀 호출
            backTracking(i + 1, idx + 1)
            
            # 치킨 거리를 세는 함수 호출
            len_chicken(i)
            
            # 초기화
            used[idx] = 0
            chicken_lst.pop()
            


N, M = map(int, input().split())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 좌표 찾기
home = []
chicken = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

home_idx = len(home)
chicken_idx = len(chicken)
used = [0] * chicken_idx
chicken_lst = []
min_len_city_chicken = 1e9

backTracking(0, 0)

print(min_len_city_chicken)