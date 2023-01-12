# 간단한 N의 약수
N = int(input())
N_lst = []
for i in range(1, N+1):
    if N % i == 0:
        N_lst.append(i)
print(*N_lst)    