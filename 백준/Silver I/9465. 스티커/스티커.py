import sys

input = sys.stdin.readline

# (1) dfs 활용
# # 0, 1, 2 순회
# def dfs(idx, prev, sum_val):
#     global result

#     if idx == n:
#         result = max(result, sum_val)
#         return

#     # 1. 스티커를 뜯지 않는 경우
#     dfs(idx + 1, -1, sum_val)

#     # 2. 0번 행의 스티커를 뜯는 경우
#     if prev != 0:
#         dfs(idx + 1, 0, sum_val + arr[0][idx])

#     # 3. 1번 행의 스티커를 뜯는 경우
#     if prev != 1:
#         dfs(idx + 1, 1, sum_val + arr[1][idx])


# T = int(input())
# for _ in range(T):
#     n = int(input())

#     arr = [list(map(int, input().split())) for _ in range(2)]

#     result = 0

#     dfs(0, -1, 0)

#     print(result)


# (2) dp 활용

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))

    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        if n == 2:
            print(max(dp[0][1], dp[1][1]))

        else:
            for i in range(2, n):
                dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
                dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

            print(max(dp[0][n - 1], dp[1][n - 1]))