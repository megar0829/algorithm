import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = 0  # 최대 숫자를 저장할 변수
cnt = 0 # 각 활잡이가 처치한 숫자를 저장할 변수
archer = arr[0]  # 활잡이(높은 숫자)를 저장
for i in range(1, N):
    if archer > arr[i]: # 뒤에 적을 잡을 경우 1 증가
        cnt += 1
    else:   # 잡지 못 할 경우(뒤에 숫자가 더 클 경우)
        archer = arr[i] # 활잡이(높은 숫자)를 다음 index로 변경
        cnt = 0  # 처치한 숫자 초기화

    if result < cnt:    # 최대 숫자 저장
        result = cnt
print(result)