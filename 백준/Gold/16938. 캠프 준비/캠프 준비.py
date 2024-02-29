from itertools import combinations

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for i in range(2, N + 1):
     for comb in combinations(arr, i):
          if L <= sum(comb) <= R and (max(comb) - min(comb)) >= X:
               cnt += 1

print(cnt)