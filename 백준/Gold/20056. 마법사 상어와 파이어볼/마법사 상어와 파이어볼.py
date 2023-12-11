N, M, K = map(int, input().split())
fire = []
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fire.append((r, c, m, s, d))

graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for _ in range(K):
    for r, c, m, s, d in fire:
        nr = (r + s * dx[d]) % N 
        nc = (c + s * dy[d]) % N
        graph[nr][nc].append([m, s, d])

    fire = []
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                cnt_m, cnt_s = 0, 0 
                odd, even = 0, 0
                cnt = len(graph[i][j])
                
                for m, s, d in graph[i][j]:
                    cnt_m += m
                    cnt_s += s
                    
                    if d % 2:
                        odd += 1
                    else:
                        even += 1
                   
                graph[i][j] = []
                        
                if odd == cnt or even == cnt: 
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                    
                if cnt_m // 5:
                    for d in nd:
                        fire.append([i, j, cnt_m // 5, cnt_s // cnt, d])

            elif len(graph[i][j]) == 1:
                fire.append([i, j] + graph[i][j].pop())

result = 0
for r, c, m, s, d in fire:
    result += m

print(result)