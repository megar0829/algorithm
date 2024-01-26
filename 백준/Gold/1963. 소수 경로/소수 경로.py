from collections import deque


prime_numbers = [False, False] + [True] * (9999)

for i in range(2, 10001):
    if prime_numbers[i]:  
        for j in range(i * 2, 10001, i):
            prime_numbers[j] = False
       
             
def bfs(num):
    global rlt
    
    que = deque([num])
    visited[int(num)] = 1
    
    while que:
        now = que.popleft()
        
        if now == after_num:
            break
        
        for i in range(4):
            if now[i] != after_num[i]:
                for n in range(10):
                    if not n and not i:
                        continue
                    
                    if now[i] != str(n):
                        next = now[:i] + str(n) + now[i + 1:]
                        if prime_numbers[int(next)] and not visited[int(next)]:
                            que.append(next)
                            visited[int(next)] = visited[int(now)] + 1
            
                             
T = int(input())
for tc in range(T):
    before_num, after_num = input().split()
    
    rlt = 0
    
    visited = [0] * (10001)
    
    if before_num != after_num:
        bfs(before_num)
        
    print(max(visited[int(after_num)] - 1, 0))