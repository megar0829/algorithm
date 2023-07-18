t = int(input())
for _ in range(t):
    n = int(input())
    markets = list(map(int, input().split()))
    print(2 * ((max(markets)) - min(markets)))