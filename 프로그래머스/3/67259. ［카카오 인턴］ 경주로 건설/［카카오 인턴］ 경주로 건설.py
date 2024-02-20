def solution(board):
    N = len(board)
    answer = 1e9

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    dp = [[1e9] * N for _ in range(N)]

    def dfs(i, j, sum_val, dir):
        nonlocal answer
        
        if (i, j) == (N - 1, N - 1):
            answer = min(answer, sum_val)
            return

        if (dp[i][j] + 500) <= sum_val: 
            return
        
        else:
            dp[i][j] = min(dp[i][j], sum_val)

        for k in range(4):
            di, dj = direction[k]
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and not board[ni][nj]:
                if dir == k:
                    save_val = 100
                
                else:
                    save_val = 600
                
                dfs(ni, nj, sum_val + save_val, k)

    dfs(0, 0, 0, 0)
    dfs(0, 0, 0, 1)
    
    return answer