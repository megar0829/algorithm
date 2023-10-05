def divide(row, col, size, max_num, term):
    if size == 1:
        cnt = 0
        for di, dj in [(1, 1), (1, 0), (0, 1), (0, 0)]:
            ni, nj = row + di, col + dj
            if (ni, nj) == (r, c):
                print(max_num - cnt)
                return
            cnt += 1
    else:
        if (row, col) == (r, c):
            print(max_num - (term * 4) + 1)
            return

        c_i, c_j = row + (2 ** size) // 2, col + (2 ** size) // 2

        # print(f'row : {row}, col : {col}, max_num : {max_num}, term : {term}')
        # print(f'center i, j : {c_i, c_j}')
        if r < c_i and c < c_j:
            # 좌상
            divide(row, col, size - 1, max_num - term * 3, term // 4)
        elif r < c_i and c >= c_j:
            # 우상
            divide(row, col + (2 ** (size - 1)), size - 1, max_num - term * 2, term // 4)
        elif r >= c_i and c < c_j:
            # 좌하
            divide(row + (2 ** (size - 1)), col, size - 1, max_num - term, term // 4)
        else:
            # 우하
            divide(row + (2 ** (size - 1)), col + (2 ** (size - 1)), size - 1, max_num, term // 4)


N, r, c = map(int, input().split())
cnt = 0

divide(0, 0, N, 2 ** (N * 2) - 1, 2 ** ((N - 1) * 2))

