import sys
input = sys.stdin.readline


def delete(idx):
    l_node, r_node = idx * 2, (idx * 2) + 1
    if l_node > l and r_node > l:
        return
    if arr[idx] < arr[l_node] and arr[idx] < arr[r_node]:
        if arr[l_node] < arr[r_node]:
            arr[r_node], arr[idx] = arr[idx], arr[r_node]
            delete(r_node)
        else:
            arr[l_node], arr[idx] = arr[idx], arr[l_node]
            delete(l_node)
    elif arr[idx] < arr[l_node]:
        arr[l_node], arr[idx] = arr[idx], arr[l_node]
        delete(l_node)
    elif arr[idx] < arr[r_node]:
        arr[r_node], arr[idx] = arr[idx], arr[r_node]
        delete(r_node)
    else:
        return


def insert(idx):
    if idx == 1:
        return
    p_node = idx // 2
    if arr[p_node] > arr[idx]:
        return
    else:
        arr[p_node], arr[idx] = arr[idx], arr[p_node]
        insert(p_node)


N = int(input())
arr = [0] * (N + 1)
l = 0
for _ in range(N):
    x = int(input())
    if x == 0:
        if l == 0:
            print(0)
        else:
            print(arr[1])
            if l > 1:
                arr[1], arr[l] = arr[l], arr[1]
                arr[l] = 0
                l -= 1
                if l > 1:
                    delete(1)
            else:
                arr[l] = 0
                l -= 1
    else:
        l += 1
        arr[l] = x
        insert(l)
