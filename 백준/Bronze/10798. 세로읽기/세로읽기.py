def print_text(input_arr, n):
    global end_cnt, result
    try:    # 리스트를 탐색하며 만약 값이 있다면 결과값에 추가하고 
        result += input_arr[n]
    except IndexError:  # 없다면 종료 조건을 1 증가
        end_cnt += 1


arr = [list(input()) for _ in range(5)]  # 2차원 배열로 세팅
n = 0        # 리스트를 탐색할 index
end_cnt = 0  # 종료 조건
result = ''  # 결과값

while True:
    if end_cnt >= 56:  # 한 줄에 최소 1개에서 15개의 문자이므로
        break  # 1,1,1,1,15 인 상황이 최대라고 생각해서 14 * 4 = 56
    # 열 우선 탐색 - 만약 값이 없다면 종료조건 + 1
    for i in range(5):
        print_text(arr[i], n)
    n += 1  # 다음 index 탐색 
    
print(result)