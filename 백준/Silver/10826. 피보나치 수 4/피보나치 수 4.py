# DP
arr = [0, 1] + [0] * (9999)
for i in range(2, 10001):
    arr[i] = arr[i - 1] + arr[i - 2]
    
N = int(input())
print(arr[N])