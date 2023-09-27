import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] * 10001
dp[0] = 1

# i : coin 의 종류
for i in coin:
    # 1 ~ k 까지 탐색하며
    # 1원 부터 k원 까지 각 금액에 대해서
    # 모든 coin 으로 만들 수 있는 경우의 수를 모두 구한다.
    # 금   액 :  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 경우의수 : [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])