T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = []
    for i in range(N):
        student = list(map(int, input().split()))
        lst.append(student[0]*0.35 + student[1]*0.45 + student[2]*0.2)
    sorted_lst = sorted(lst, reverse=True)
    dict_student = {}
    for j in range(N):
        dict_student[sorted_lst[j]] = grades[j//(N//10)]
    print(f'#{t} {dict_student[lst[K-1]]}')