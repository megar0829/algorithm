N, X = map(int, input().split())
arr = list(map(int, input().split()))

max_val = 0
max_cnt = 1
save_val = 0
for i in range(X):
    save_val += arr[i]
max_val = save_val

for i in range(X, N):
    save_val -= arr[i - X]
    save_val += arr[i]
    if max_val < save_val:
        max_val = save_val
        max_cnt = 1
    elif max_val == save_val:
        max_cnt += 1
if max_val == 0:
    print('SAD')
else:
    print(max_val)
    print(max_cnt)