arr = [0] * 10
for _ in range(5):
    n = int(input())
    arr[n] += 1

for i in range(10):
    if arr[i] == 1 or arr[i] == 3 or arr[i] == 5:
        print(i)
