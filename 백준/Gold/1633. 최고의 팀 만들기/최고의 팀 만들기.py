import sys
input = sys.stdin.readline

player = []

while True:
    try:
        white, black = map(int, input().split())
        player.append((white, black))
    
    except:
        break
    
dp = [[0] * 16 for _ in range(16)]

for white, black in player:
    for w in range(15, -1, -1):
        for b in range(15, -1, -1):
            if w:
                dp[w][b] = max(dp[w][b], dp[w - 1][b] + white)
                
            if b:
                dp[w][b] = max(dp[w][b], dp[w][b - 1] + black)

print(dp[15][15])