# 연산자에 따라서 연산자 양 옆의 값들을 계산 해주는 함수
def calculator(left_val, right_val, operator):
    if operator == '+':
        return left_val + right_val
    elif operator == '-':
        return left_val - right_val
    elif operator == '*':
        return left_val * right_val
    else:
        # 둘 중에 한 개가 음수라면 양수인 상태로 연산 후 - 부호를 붙여주기
        if left_val < 0 or right_val < 0:
            return (-1) * (abs(left_val) // abs(right_val))
        return left_val // right_val


def backTracking(i):
    if i == M:
        sum_val = arr[0]
        for j in range(M):
            sum_val = calculator(sum_val, arr[j + 1], calculations[path[j]])
        result.append(sum_val)
        return

    for j in range(M):
        if j not in path:
            path[i] = j
            backTracking(i + 1)
            path[i] = -1


N = int(input())
arr = list(map(int, input().split()))


# 연산자의 개수에 맞춰서 연산자를 담은 calculations 배열 생성
cal_cnt = list(map(int, input().split()))
calculations = []
i = 0
for cal in '+-*/':
    for cnt in range(cal_cnt[i]):
        calculations.append(cal)
    i += 1
    
M = len(calculations)   # 연산자의 개수
path = [-1] * M         # calculations 의 index 를 담을 배열
result = []

backTracking(0)

print(max(result))
print(min(result))
