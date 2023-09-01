def bin_to_int(arr, n):
    val = 0
    for i in range(n):
        if arr[i] == 1:
            val += 2 ** ((n - 1) - i)
    return val


def trit_to_int(arr, m):
    val = 0
    for i in range(m):
        if arr[i] != 0:
            val += arr[i] * (3 ** ((m - 1) - i))
    return val


T = int(input())
bin_dict = {
    0: 1,
    1: 0
}
trit_dict = {
    0: [1, 2, 0],
    1: [2, 0, 1],
    2: [0, 1, 2]
}
for tc in range(1, T + 1):
    bin_num = list(map(int, input()))
    N = len(bin_num)
    trit_num = list(map(int, input()))
    M = len(trit_num)

    result = []
    for i in range(N):
        bin_num[i] = bin_dict[bin_num[i]]
        result.append(bin_to_int(bin_num, N))
        bin_num[i] = bin_dict[bin_num[i]]

    flag = False
    for i in range(M):
        trit = trit_num[i]
        for j in range(3):
            trit_num[i] = trit_dict[trit][j]
            if j != 2:
                save_val = trit_to_int(trit_num, M)
                if save_val in result:
                    print(f'#{tc} {save_val}')
                    flag = True
                    break
        if flag:
            break