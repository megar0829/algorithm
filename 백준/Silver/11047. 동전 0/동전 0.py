import sys
N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin = sorted(coin, reverse=True)
cnt = 0
for i in coin:
    cnt += K // i
    K %= i
print(cnt)