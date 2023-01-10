T = int(input())

for i in range(1, T+1):
    n = list(map(int, input().split()))
    result = sum(n) / len(n)
    print(f'#{i} {round(result)}')