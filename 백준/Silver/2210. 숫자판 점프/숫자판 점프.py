def backTracking(i, j, idx):
    global save_digit
    if idx == 6:
        result.add(save_digit[:])
        return
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            save_digit += arr[ni][nj]
            backTracking(ni, nj, idx + 1)
            save_digit = save_digit[:idx]


arr = [list(input().split()) for _ in range(5)]

result = set()
save_digit = ''
for x in range(5):
    for y in range(5):
        backTracking(x, y, 0)
print(len(result))

