T = int(input())
for t in range(1, T+1):
    A = list(map(int ,input().split()))
    print(sorted(A, reverse=True)[2])