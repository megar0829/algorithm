from collections import deque
import sys
input = sys.stdin.readline

# ## bfs 사용
# def bfs():
#     que = deque([(1, False)])
    
#     while que:
#         now, flag = que.popleft()
        
#         for val in [1, 2, 3]:
#             next = now + val
            
#             if next > N:
#                 continue
            
#             if val == 1:
#                 if not visited[next] or visited[next] > visited[now] + small_jump[now]:
#                     que.append((next, flag))
#                     visited[next] = visited[now] + small_jump[now]
            
#             elif val == 2:
#                 if not visited[next] or visited[next] > visited[now] + big_jump[now]:
#                     que.append((next, flag))
#                     visited[next] = visited[now] + big_jump[now]
                        
#             elif val == 3:
#                 if flag:
#                     continue
                
#                 if not visited[next] or visited[next] > visited[now] + k:
#                     que.append((next, True))
#                     visited[next] = visited[now] + k

# N = int(input())

# small_jump = [0] * N
# big_jump = [0] * N

# for i in range(1, N):
#     a, b = map(int, input().split())
    
#     small_jump[i] = a
#     big_jump[i] = b
    
# k = int(input())

# visited = [0] * (N + 1)

# bfs()

# print(visited[N])

# dp 사용

N = int(input())

small_jump = [0] * (N - 1)
big_jump = [0] * (N - 1)

for i in range(N - 1):
    a, b=map(int,input().split())

    small_jump[i] = a
    big_jump[i] = b

k = int(input())

if N == 1:
    print(0)
    
elif N == 2:
    print(small_jump[0])
    
else:
    dp = [0] * N

    dp[1] = small_jump[0]
    dp[2] = min(small_jump[0] + small_jump[1], big_jump[0])
    
    for i in range(3, N):
        dp[i] = min(small_jump[i - 1] + dp[i - 1], big_jump[i - 2] + dp[i - 2])

    ans = dp[-1]
    
    dp_copy = dp[:]

    for i in range(0, N - 3):
        if dp[i] + k < dp[i + 3]:
            dp_copy[i + 3] = dp[i] + k
            
            for j in range(i + 4, N):
                dp_copy[j] = min(dp[j], dp_copy[j - 1] + small_jump[j-1], dp_copy[j-2] + big_jump[j - 2])
            
            if dp_copy[-1] < ans:
                ans = dp_copy[-1]
    print(ans)