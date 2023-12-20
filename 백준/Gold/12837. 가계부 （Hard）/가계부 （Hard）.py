import sys
input = sys.stdin.readline

    
def update_seg(node, start, end, idx, val):
    if idx < start or end < idx:
        return
    
    if start == end:
        tree[node] += val
        return
    
    update_seg(node * 2, start, (start + end) // 2, idx, val)
    update_seg((node * 2) + 1, ((start + end) // 2) + 1, end, idx, val)
    
    tree[node] = tree[node * 2] + tree[(node * 2) + 1]


def sub_sum_seg(node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    return sub_sum_seg(node * 2, start, (start + end) // 2, left, right) + sub_sum_seg((node * 2) + 1, ((start + end) // 2) + 1, end, left, right)


N, Q = map(int, input().split())

tree = [0] * (4 * N)

for _ in range(Q):
    
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        p, x = query[1], query[2]
        update_seg(1, 0, N - 1, p - 1, x)        
    
    elif query[0] == 2:
        p, q = query[1], query[2]
        print(sub_sum_seg(1, 0, N - 1, p - 1, q - 1))