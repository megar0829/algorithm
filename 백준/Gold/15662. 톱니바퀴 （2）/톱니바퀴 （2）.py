import sys
input = sys.stdin.readline


def turn_gear(idx, direc):
    save_gear = arr[idx][:]
    move(idx, direc)
    visited[idx] = True
    
    if idx == 0:
        if not visited[idx + 1]:
            if arr[idx + 1][6] != save_gear[2]:
                turn_gear(idx + 1, direc * (-1))
    
    elif idx == T - 1:
        if not visited[idx - 1]:
            if arr[idx - 1][2] != save_gear[6]:
                turn_gear(idx - 1, direc * (-1))
    
    else:
        if not visited[idx + 1]:
            if arr[idx + 1][6] != save_gear[2]:
                turn_gear(idx + 1, direc * (-1))
    
        if not visited[idx - 1]:
            if arr[idx - 1][2] != save_gear[6]:
                turn_gear(idx - 1, direc * (-1))
        

def move(i, d):
    if d == -1:
        save_val = arr[i][1:] + arr[i][0]
        arr[i] = save_val
    elif d == 1:
        save_val = arr[i][7] + arr[i][:7]
        arr[i] = save_val
    

T = int(input())

arr = [input().strip('\n') for _ in range(T)]

K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    
    visited = [False] * T
    turn_gear(num - 1, direction)
    
cnt = 0
for i in range(T):
    if arr[i][0] == '1':
        cnt += 1
        
print(cnt)