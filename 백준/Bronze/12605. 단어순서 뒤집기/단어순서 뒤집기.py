n = int(input())
for x in range(1, n + 1):
    text = list(map(str, input().split()))
    print(f'Case #{x}:', *text[::-1])