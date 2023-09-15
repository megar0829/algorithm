import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    text = input().strip('\n')
    if len(text) >= M:
        arr.setdefault(text, 0)
        arr[text] += 1

result = {}
for k, v in arr.items():
    result.setdefault(v, [])
    result[v].append(k)

for k in sorted(result.keys(), reverse=True):
    for v in sorted(result[k], key=lambda x:(-len(x), x)):
        print(v)