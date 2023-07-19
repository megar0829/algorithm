T = int(input())
for _ in range(T):
    numbers = list(map(int, input().split()))
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    print(sum(even), min(even))
