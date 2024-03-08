import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import combinations, permutations

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

turn_idx = [list(map(int, input().split())) for _ in range(K)]

ans = 1e9

for turn_lst in permutations(turn_idx, K):
    A_copy = deepcopy(A)
    
    for r, c, s in turn_lst:
        r, c = r - 1, c - 1
        
        for n in range(s, 0, -1):
            tmp = A_copy[r - n][c + n]
            
            A_copy[r - n][(c - n) + 1 : (c + n) + 1] = A_copy[r - n][(c - n) : (c + n)]
            
            for row in range(r - n, r + n):
                A_copy[row][c - n] = A_copy[row + 1][c - n]
                
            A_copy[r + n][(c - n) : (c + n)] = A_copy[r + n][(c - n) + 1 : (c + n) + 1]
            
            for row in range(r + n, r - n, -1):
                A_copy[row][c + n] = A_copy[row - 1][c + n]
                
            A_copy[(r - n) + 1][c + n] = tmp

    
    for i in range(N):
        ans = min(ans, sum(A_copy[i]))

print(ans)