N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

result = []

# 8 * 8 사각형의 크기를 제외한 전체를 탐색하며
for i in range(N - 7):
    for j in range(M - 7):
        
        # cnt1: W 로 시작하는 체스판의 경우 일치하는 개수
        # cnt2: B 로 시작하는 체스판의 경우 일치하는 개수
        cnt1 = cnt2 = 0
        
        # 8*8 배열을 탐색하며 일치하는 개수 count
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2:
                    if arr[x][y] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[x][y] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        
        # 두 개의 시작점에서 탐색한 결과 중
        # 더 작은 값을 저장 (수정해야 하는 개수)
        result.append(min(cnt1, cnt2))
        
print(min(result))