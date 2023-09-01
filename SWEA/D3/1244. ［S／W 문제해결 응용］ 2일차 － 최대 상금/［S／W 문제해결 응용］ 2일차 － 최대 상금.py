# 완전탐색 - 가지치기
def back_track(repeat):
    global ans
    val = int(''.join(P))  # 숫자 카드

    if val in visited[repeat]:
        return
    visited[repeat].add(val)  # 검사 전이라면 패턴을 추가

    if repeat == r:  # 교환횟수를 모두 사용 했다면,
        ans = max(val, ans)  # 최대 상금 갱신

    else:  # 교환횟수가 남아 있다면
        for i in range(N - 1):
            for j in range(i + 1, N):
                # 변경하고
                P[i], P[j] = P[j], P[i]
                # 확인
                back_track(repeat + 1)
                # 원상 복구
                P[i], P[j] = P[j], P[i]


T = int(input())
for tc in range(1, T + 1):

    P, r = map(int, input().split())  # 숫자 패턴 P, 교환 횟수 r
    P = list(str(P))
    N = len(P)  # 숫자 카드의 길이
    visited= [set() for _ in range(11)]  # 최대 교환이 10 // set 으로 중복을 없앤다.
    ans = 0

    back_track(0)
    print(f'#{tc} {ans}')