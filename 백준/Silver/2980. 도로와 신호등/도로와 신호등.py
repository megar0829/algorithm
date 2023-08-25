import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [0] * (L + 1)
sign = [[] for _ in range(L + 1)]
for _ in range(N):
    D, R, G = list(map(int, input().split()))
    sign[D].append(R)
    sign[D].append(G)

time = 0
for i in range(1, L + 1):
    time += 1
    if sign[i]:
        if time <= sign[i][0]:
            time += sign[i][0] - time
        else:
            if time > sign[i][0] + sign[i][1]:
                save_i = time % (sign[i][0] + sign[i][1])
                if save_i <= sign[i][0]:
                    time += sign[i][0] - save_i
print(time)