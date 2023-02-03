T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    numbers = [i for i in range(1,N+1)]
    for i in lst:
        numbers.pop(numbers.index(i))
    print(f'#{t}', *numbers)