T = int(input())
for x in range(1, T + 1):
    num1, num2 = map(int, input().split())
    print(f'Case {x}: {num1 + num2}')