def dfs(now, arr):
    if not arr:
        return

    min_alp = min(arr)

    start_idx = arr.index(min_alp)

    result[now + start_idx] = min_alp

    print("".join(result))

    dfs(now + start_idx + 1, arr[start_idx + 1:])
    dfs(now, arr[:start_idx])


word = list(input())

l = len(word)

result = [""] * l

dfs(0, word[:])