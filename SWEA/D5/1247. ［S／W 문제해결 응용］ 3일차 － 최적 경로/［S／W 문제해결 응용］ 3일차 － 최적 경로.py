def dist(lst, n):
    save_dist = abs(o1 - arr[lst[0]][0]) + abs(o2 - arr[lst[0]][1])
    for i in range(1, n):
        save_dist += abs(arr[lst[i - 1]][0] - arr[lst[i]][0]) + abs(arr[lst[i - 1]][1] - arr[lst[i]][1])
    save_dist += abs(arr[lst[n - 1]][0] - h1) + abs(arr[lst[n - 1]][1] - h2)
    return save_dist


def case(i, n, used, customer):
    global min_val
    if i == n:
        save_val = dist(customer, n)
        min_val = min(min_val, save_val)
        return
    else:
        for j in range(n):
            if not used[j]:
                customer[i] = j
                used[j] = 1
                case(i + 1, n, used, customer)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    o1, o2, h1, h2, *data = list(map(int, input().split()))
    arr = [[] for _ in range(N)]
    for i in range(N):
        arr[i] = [data[i * 2], data[i * 2 + 1]]
    used = [0] * N
    customer = [0] * N
    min_val = 10000000
    case(0, N, used, customer)
    print(f'#{tc} {min_val}')