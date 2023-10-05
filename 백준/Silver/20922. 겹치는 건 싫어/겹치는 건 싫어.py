from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

used = [0] * (max(arr) + 1)
max_cnt = 0
cnt = 0
result = deque()
for i in range(N):
    if used[arr[i]] < K:
        cnt += 1
        used[arr[i]] += 1
        result.append(arr[i])
    else:
        max_cnt = max(max_cnt, cnt)
        cnt += 1
        used[arr[i]] += 1
        result.append(arr[i])
        for _ in range(cnt):
            save_val = result.popleft()
            used[save_val] -= 1
            cnt -= 1
            if save_val == arr[i]:
                break
max_cnt = max(max_cnt, cnt)

print(max_cnt)