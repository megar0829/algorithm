N = int(input())
factorial = 1
for i in range(1, N + 1):
    factorial *= i
zero_cnt = 0
for i in str(factorial)[::-1]:
    if i == '0':
        zero_cnt += 1
    else:
        break
print(zero_cnt)