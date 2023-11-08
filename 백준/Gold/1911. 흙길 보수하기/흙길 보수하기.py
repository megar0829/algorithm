import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pool = []
for _ in range(N):
    s, e = map(int, input().split())
    pool.append((s, e))

pool.sort()

save_val = 0
result = 0

for start, end in pool:
    if save_val > start:
        start = save_val

    s, r = (end - start) // L, (end - start) % L

    if r == 0:
        result += s
        save_val = start + L * s
    else:
        result += s + 1
        save_val = start + L * (s + 1)

print(result)
