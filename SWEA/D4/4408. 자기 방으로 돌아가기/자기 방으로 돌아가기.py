T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 학생 수
    arr = [0] * 201   # 방 사이 공간을 지나는사람 수
    for _ in range(N):
        f, t = map(int, input().split())
        f = (f + f % 2) // 2
        t = (t + t % 2) // 2
        for i in range(min(f, t), max(f, t) + 1):
            arr[i] += 1
    print(f'#{tc} {max(arr)}')