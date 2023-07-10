N = int(input())
matrix = [[0]*101 for _ in range(101)]
for i in range(N):
    A, B = map(int, input().split())
    for i in range(A, A + 10):
        for j in range(B, B + 10):
            matrix[i][j] = 1
result = 0
for i in matrix:
    result += sum(i)
print(result)