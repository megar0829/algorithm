# 현재 위치에서 대각선에 겹치는 queen 이 있는지 확인하는 함수
def check_queen(R):     # R: 현재 행의 번호
    for r in range(R):  # 0 ~ 현재 행 까지 탐색 (R 이후 행은 아직 queen 이 없기때문)

        '''
        이전 행과 현재 행에 있는 queen 의 column 번호가 같거나,
        이전 행의 queen 좌표 : (r, c), 현재 행의 queen 좌표 : (R, C) 일때
        좌표가 대각선 아래로 이동하기 위해서는 (i, j) = > (i + 1, j + 1) or (i + 1, j - 1)
        즉, 행이 1 씩 증가하고 열이 1 씩 증가하거나 감소해야 하므로
        두 개의 좌표가 같은 대각선 상에 존재하려면
        [(현재 행의 col) 와 (이전 행의 col) 의 차이] 와 [(현재 행의 row) 와 (이전 행의 row) 의 차이] 가 같아야 한다.
        현재 행의 row 값은 항상 이전 행의 row 값 보다 크기 때문에 column 값에만 절대값을 적용 
        '''

        # 같은 대각선 상에 queen 이 존재한다면 False, 없으면 True 반환
        if row[R] == row[r] or abs(row[R] - row[r]) == R - r:
            return False
    return True


# 행과 열을 이동하며 겹치지 않는 장소에 queen 을 놓는 함수
def backTracking(i):
    global cnt

    # 마지막까지 퀸을 뒀다면 return
    if i == N:
        cnt += 1
        return

    # col 값을 탐색하며
    for j in range(N):
        # 해당 열에 퀸을 뒀다면 pass
        if col[j]:
            continue

        # 현재 행에서 퀸의 위치를 i, j 로 두고
        row[i] = j

        # i, j 를 기준으로 대각선에 퀸이 이미 있는지 확인
        if check_queen(i):
            # 퀸을 놓을 수 있다면, 현재 열에 사용처리 (재귀 들어가기 전 로직 - 경로 저장)
            col[j] = 1

            # 다음 행으로 이동 (재귀 함수 호출)
            backTracking(i + 1)

            # 놓았던 퀸을 해당 열에서 제거 (돌아와서 초기화)
            col[j] = 0


N = int(input())

cnt = 0

# row 배열의 값 : 각 항목의 index 는 행을 나타내며 value 는 각 행에서 queen 이 위치하는 column 번호
row = [0] * N

# col 배열의 값 : 각 항목의 index 는 열을 나타내며 value 는 각 열에 queen 이 존재하는지 여부를 나타냄
col = [0] * N

backTracking(0)

print(cnt)