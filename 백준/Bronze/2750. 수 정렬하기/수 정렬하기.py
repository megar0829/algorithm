N = int(input())
A = [int(input()) for i in range(N)]
print(*sorted(A), sep='\n')