import sys
input = sys.stdin.readline
from copy import deepcopy

S = input().strip('\n')
q = int(input())

dp_dict = [{} for _ in range(len(S) + 1)]
for i in range(len(S)):
    dp_dict[i + 1] = deepcopy(dp_dict[i])
    dp_dict[i + 1][S[i]] = dp_dict[i + 1].get(S[i], 0) + 1

for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    print(dp_dict[r + 1].get(alpha, 0) - dp_dict[l].get(alpha, 0))
