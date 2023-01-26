T = int(input())
for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.pop(numbers.index(max(numbers)))
    numbers.pop(numbers.index(min(numbers)))
    print(f'#{i} {round(sum(numbers) / len(numbers))}')