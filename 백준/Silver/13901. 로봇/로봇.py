import sys
input = sys.stdin.readline

# 2% 실패

# R, C = map(int, input().split())
# k = int(input())

# visited = [[False] * C for _ in range(R)]

# for _ in range(k):
#     br, bc = map(int, input().split())
    
#     visited[br][bc] = True
    
# sr, sc = map(int, input().split())

# visited[sr][sc] = True

# d = []

# direction = list(map(int, input().split()))

# for idx in direction:
#     if idx == 1:
#         d.append((-1, 0))
#     elif idx == 2:
#         d.append((1, 0))
#     elif idx == 3:
#         d.append((0, -1))
#     elif idx == 4:
#         d.append((0, 1))

# cnt = 0
# idx = 0

# ans = (sr, sc)

# while True:
#     if cnt == 4:
#         print(*ans)
#         break
    
#     r, c = sr + d[direction[idx] - 1][0], sc + d[direction[idx] - 1][1]
    
#     if 0 <= r < R and 0 <= c < C and not visited[r][c]:
#         visited[r][c] = True
        
#         sr, sc = r, c
        
#         cnt = 0
        
#         ans = (sr, sc)
    
#     else:
#         cnt += 1
#         idx = (idx + 1) % 4


r, c = map(int, input().split())
data = [ [0] * c for _ in range(r)]

k = int(input())
for _ in range(k):
  kr, kc = map(int, input().split())
  data[kr][kc] = -1

x, y = map(int, input().split())
data[x][y] = 1

dir = list(map(int, input().split()))

last = [x, y]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

pos = 0
cnt = 0
while True:
  if cnt == 4:
    break
  pos = pos%4
  nx = x + dx[dir[pos]]
  ny = y + dy[dir[pos]]
  if nx < 0 or nx >= r or ny < 0 or ny >= c or data[nx][ny] != 0:
    pos += 1
    cnt += 1
  else:
    cnt = 0
    data[nx][ny] = data[x][y]+1
    x = nx
    y = ny
    last = [x, y]
print(last[0], last[1])