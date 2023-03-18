T = int(input())
for t in range(1, T+1):
    a, b, c, d = list(map(int, input().split()))
    hour = a + c
    minute = b + d
    while True:
        if hour > 12:
            hour -= 12
        elif minute > 60:
            minute -= 60
            hour += 1
        elif hour <= 12 and minute <= 60:
            break
    print(f'#{t} {hour} {minute}')