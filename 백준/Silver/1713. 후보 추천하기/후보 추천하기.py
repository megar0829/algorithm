N = int(input())
t = int(input())
data = list(map(int, input().split()))
student = [0] * 101
que = []
for i in range(t):
    if len(que) < N:
        if not student[data[i]]:
            student[data[i]] = 1
            que.append(data[i])
        else:
            student[data[i]] += 1
    else:
        if student[data[i]]:
            student[data[i]] += 1
        else:
            min_cnt = 10000
            min_idx = 0
            for j in range(N):
                if min_cnt > student[que[j]]:
                    min_cnt = student[que[j]]
                    min_idx = j
            student[que.pop(min_idx)] = 0
            student[data[i]] = 1
            que.append(data[i])
print(*sorted(que))