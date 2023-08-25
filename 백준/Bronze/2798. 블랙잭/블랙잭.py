N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_card = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            save_card = arr[i] + arr[j] + arr[k]
            if max_card < save_card <= M:
                max_card = save_card

print(max_card)