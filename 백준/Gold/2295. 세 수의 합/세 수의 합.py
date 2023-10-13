import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

sum_ab = set()

for a in range(N):
    for b in range(N):
        sum_ab.add(arr[a] + arr[b])

result = 0

for k in range(N - 1, -1, -1):
    for c in range(N - 1, -1, -1):
        minus_kc = arr[k] - arr[c]
        if minus_kc in sum_ab:
            result = minus_kc + arr[c]
            break
    if result:
        break

print(result)
