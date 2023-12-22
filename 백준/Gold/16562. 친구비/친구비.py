import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x, y = find_set(x), find_set(y)
    
    if friend_fee[x] > friend_fee[y]:
        friend_fee[x] = 0
        parent[x] = y
        
    else:
        friend_fee[y] = 0
        parent[y] = x


N, M, k = map(int, input().split())

friend_fee = [0] + list(map(int, input().split()))

parent = list(range(N + 1))

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

ans = sum(friend_fee)

if ans <= k:
    print(ans)

else:
    print('Oh no')