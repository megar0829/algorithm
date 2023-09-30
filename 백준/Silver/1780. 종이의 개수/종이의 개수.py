import sys
input = sys.stdin.readline

# 종이 안에 같은 다른 숫자가 있는지 확인하는 함수
# 다른 숫자가 발견되면 False, 모두 같은 숫자면 True
def check(n, m, K):
    prev_val = arr[n][m]
    for i in range(n, n + K):
        for j in range(m, m + K):
            if arr[i][j] != prev_val:
                return False
    return True

# 종이 안에 같은 숫자가 있으면 개수 count
# 다른 숫자가 있다면 같은 크기의 종이 9 개로 나눠서
# 다시 확인 후 개수 count
def count_num(start_i, start_j, size):
    global cnt_minus, cnt_zero, cnt_plus
    
    if check(start_i, start_j, size):
        if arr[start_i][start_j] == -1:
            cnt_minus += 1
        elif arr[start_i][start_j] == 0:
            cnt_zero += 1
        elif arr[start_i][start_j] == 1:
            cnt_plus += 1
        
    else:
        size //= 3
        
        for i in range(3):
            for j in range(3):
                count_num(start_i + (i * size), start_j + (j * size), size)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_minus = 0
cnt_zero = 0
cnt_plus = 0
count_num(0, 0, N)

print(cnt_minus)
print(cnt_zero)
print(cnt_plus)