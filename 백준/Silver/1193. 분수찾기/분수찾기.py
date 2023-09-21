num = {}
save_val = 1
for i in range(1, 4474):
    num[save_val] = i
    save_val += i
arr = sorted(num.keys())
N = 4473

X = int(input())
if X in arr:
    if num[X] % 2:
        result = str(num[X]) + '/1'
    else:
        result = '1/' + str(num[X])
else:
    for i in range(N):
        if arr[i] > X:
            j = num[arr[i - 1]]
            start = arr[i - 1]
            break
    if j % 2:
        x = j
        y = 1
        while True:
            if start == X:
                break
            x -= 1
            y += 1
            start += 1
        result = str(x) + '/' + str(y)
    else:
        x = 1
        y = j
        while True:
            if start == X:
                break
            x += 1
            y -= 1
            start += 1
        result = str(x) + '/' + str(y)
print(result)