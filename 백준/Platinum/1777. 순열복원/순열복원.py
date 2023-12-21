import sys
input = sys.stdin.readline


# Segment-Tree 생성
def create_seg(node, start, end):
    # node == leaf node 일 경우
    if start == end:
        tree[node] = 1
        return tree[node]
    
    # node != leaf node
    tree[node] = create_seg(node * 2, start, (start + end) // 2) + create_seg((node * 2) + 1, ((start + end) // 2) + 1, end)
    return tree[node]
    
    
# Segment-Tree data 수정
def update_seg(node, start, end, idx):
    # 재귀를 통해 범위를 벗어난 경우 종료 (종료 조건)
    if idx < start or idx > end:
        return
    
    tree[node] -= 1
    # node != leaf node 일 경우
    if start != end:
        # 왼쪽 자식 검사
        update_seg(node * 2, start, (start + end) // 2, idx)
        # 오른쪽 자식 검사
        update_seg((node * 2) + 1, ((start + end) // 2) + 1, end, idx)


def search_number(node, start, end, val):
    if start == end:
        return start

    if tree[(node * 2) + 1] <= val:
        return search_number(node * 2, start, (start + end) // 2, val - tree[(node * 2) + 1])
    else:
        return search_number((node * 2) + 1, ((start + end) // 2) + 1, end, val)


N = int(input())

arr = list(map(int, input().split()))

tree = [0] * (4 * N)

result = [0] * N

create_seg(1, 0, N - 1)
    
for i in range(N - 1, -1, -1):
    num = search_number(1, 0, N - 1, arr[i])
    result[num] = i + 1
    update_seg(1, 0, N - 1, num)

print(*result)