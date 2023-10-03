import sys
input = sys.stdin.readline


def check(n, m, K):
    color = arr[n][m]
    for i in range(n, n + K):
        for j in range(m, m + K):
            if arr[i][j] != color:
                return False
    return True


def divide(row, col, size):
    global white, blue
    
    if check(row, col, size):
        if arr[row][col]:
            blue += 1
        elif not arr[row][col]:
            white += 1
    else:
        size //= 2
        
        for i in range(2):
            for j in range(2):
                divide(row + (i * size), col + (j * size), size)
        

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

divide(0, 0, N)

print(white)
print(blue)