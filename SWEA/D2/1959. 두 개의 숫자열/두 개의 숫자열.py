T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int ,input().split()))
    B = list(map(int, input().split()))
    result = 0
    lst = []
    if len(A) == len(B):
        for i in range(len(A)):
            result += A[i] * B[i] 
    else:
        if len(A) > len(B):
            l = len(A) - len(B) + 1
            for i in range(l):
                s = 0
                cnt = 0
                for j in range(i, i + len(B)):
                    s += A[j] * B[cnt]
                    cnt += 1
                lst.append(s)
            result = max(lst)
        elif len(A) < len(B):
            l = len(B) - len(A) + 1
            for i in range(l):
                s = 0
                cnt = 0
                for j in range(i, i + len(A)):
                    s += B[j] * A[cnt]
                    cnt += 1
                lst.append(s)
            result = max(lst)
    print(f'#{t} {result}')