def sol_1():
    save_val = arr[0]

    result = []

    for n in range(N, 0, -1):
        factor_val = factorial[n - 1]
        idx = (save_val - 1) // factor_val
        result.append(numbers.pop(idx))
        save_val -= factor_val * idx

    return result


def sol_2():
    save_val = 1
    for n in range(N, 0, -1):
        factor_val = factorial[n - 1]
        idx = numbers.index(arr[N - n])
        numbers.pop(idx)
        save_val += factor_val * idx

    return save_val


factorial = [1] * (21)

factorial_val = 1
for n in range(1, 21):
    factorial_val *= n
    factorial[n] = factorial_val

N = int(input())

num, *arr = list(map(int, input().split()))

result = []
numbers = list(range(1, N + 1))

if num == 1:
    print(*sol_1())

elif num == 2:
    print(sol_2())