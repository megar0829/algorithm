arr = [int(input()) for _ in range(9)]
sum_arr = sum(arr)
check = False
for i in range(8):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == sum_arr - 100:
            arr.pop(j)
            arr.pop(i)
            check = True
            break
    if check:
        break

for i in sorted(arr):
    print(i)