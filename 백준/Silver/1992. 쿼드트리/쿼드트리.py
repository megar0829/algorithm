import sys
input = sys.stdin.readline

def check(n, m, size):
    color = arr[n][m]
    for i in range(n, n + size):
        for j in range(m, m + size):
            if arr[i][j] != color:
                return False
    return True


def divide(row, col, size):
    global result
    if check(row, col, size):
        if arr[row][col]:
            result += '1'
        elif not arr[row][col]:
            result += '0'
    else:
        result += '('
        size //= 2
        for i in range(2):
            for j in range(2):
                divide(row + (i * size), col + (j * size), size)
        result += ')'
                
N = int(input())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]
result = ''

divide(0, 0, N)

print(result)