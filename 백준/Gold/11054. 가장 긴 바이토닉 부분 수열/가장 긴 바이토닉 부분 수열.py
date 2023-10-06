# 11054 g4
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 오름차순
# 앞에서 부터 탐색하며 본인 숫자 앞에 더 작은 숫자가 있으면 그 숫자의 DP 값 + 1
dp_front_search = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_front_search[i] = max(dp_front_search[i], dp_front_search[j] + 1)

# 내림차순
# 뒤에서 부터 탐색하며 본인 숫자 뒤에 더 작은 숫자가 있으면 그 숫자의 DP 값 + 1
dp_back_search = [1]*N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[i] > arr[j]:
            dp_back_search[i] = max(dp_back_search[i], dp_back_search[j] + 1)

# 오름차순과 내림차순의 탐색 결과를 각 자리에서 합친 후
# 자기 자신은 두번 중복 되므로 1을 빼준다
DP = [0] * N
for i in range(N):
    DP[i] = dp_front_search[i] + dp_back_search[i] - 1

print(max(DP))