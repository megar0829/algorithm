T = int(input())
for _ in range(T):
    N = int(input())
    grades = 0
    cnt_c = 0
    for i in range(N):
        C, G = map(float, input().split())
        grades += C * G
        cnt_c += int(C)
    print(cnt_c, round(grades/cnt_c, 1))